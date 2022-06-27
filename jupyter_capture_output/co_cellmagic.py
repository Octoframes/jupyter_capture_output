from io import BytesIO
from base64 import b64decode

from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import display
from IPython.utils.capture import capture_output
from PIL import Image
from pathlib import Path
from pprint import pprint # for debugging


@magics_class
class CaptureMagic(Magics):
    @magic_arguments.magic_arguments() ################### IMAGE
    @magic_arguments.argument(
        "--path",
        "-p",
        default=None,
        help=(
            "The path where the image will be saved to. When there is more then one image, multiple paths have to be defined"
        ),
    )
    @magic_arguments.argument(
        "--compression",
        "-c",
        default=None,
        help=(
            "Defines the amount of compression,  quality can be from 0.1 - 100 , images must be .jpg"
        ),
    )
    @cell_magic
    def capture_img(self, line, cell):
        args = magic_arguments.parse_argstring(CaptureMagic.capture_img, line)
        paths = args.path.strip('"').split(" ")
        with capture_output(stdout=False, stderr=False, display=True) as result:
            self.shell.run_cell(cell)
        for output in result.outputs:
            display(output)
            data = output.data
            if "image/png" in data:
                path = paths.pop(0)
                if not path:
                    raise ValueError("Too few paths given!")
                png_bytes = data["image/png"]
                if isinstance(png_bytes, str):
                    png_bytes = b64decode(png_bytes)
                assert isinstance(png_bytes, bytes)
                bytes_io = BytesIO(png_bytes)
                img = Image.open(bytes_io)
                if args.compression:
                    if img.mode != "RGB":
                        img = img.convert("RGB")
                    img.save(path, "JPEG", optimize=True, quality=int(args.compression))
                else:
                    img.save(path, "png")

    @magic_arguments.magic_arguments() ################### TEXT
    @magic_arguments.argument(
        "--path",
        "-p",
        default=None,
        help=(
            "The path where the text will be saved to"
        ),
    )
    @cell_magic
    def capture_text(self, line, cell):
        args = magic_arguments.parse_argstring(CaptureMagic.capture_text, line)
        path = args.path.strip('"')
        with capture_output(stdout=True, stderr=False, display=False) as result:
            self.shell.run_cell(cell)
            message = result.stdout

        if len(message) == 0:
            raise ValueError("No standard output (stdout) found!")
        print(message)
        dest = Path(path)
        dest.write_text(message)


    @magic_arguments.magic_arguments() ################### Video
    @magic_arguments.argument(
        "--path",
        "-p",
        default=None,
        help=(
            "The path where the video will be saved to. When there is more then one video, multiple paths have to be defined"
        ),
    )
    @cell_magic
    def capture_video(self, line, cell):
        args = magic_arguments.parse_argstring(CaptureMagic.capture_video, line)
        paths = args.path.strip('"').split(" ")
        with capture_output(stdout=False, stderr=False, display=True) as result:
            self.shell.run_cell(cell)
        for output in result.outputs:
            display(output) # only disabled for debugging
            global data # for debugging 
            data = output.data

            # pprint(data) # for debugging 

            if "text/html" in data: # this is not nice, is there any better way to access IPython.core.display.Video object ?
                path = paths.pop(0)
                if not path:
                    raise ValueError("Too few paths given!")
                video_object = data["text/html"]
                split_string = video_object.split('"')
                video_url = split_string[1]
                # print(video_url) # for debugging 
                # print(path) # for debugging 

                dest = Path(path)
                src = Path(video_url)
                dest.write_bytes(src.read_bytes())
                