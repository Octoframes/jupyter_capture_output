from io import BytesIO
from base64 import b64decode

from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import display
from IPython.utils.capture import capture_output
from PIL import Image
from pathlib import Path
from pprint import pprint # for debugging
import re


def path_preprocessing(path):
    # print(type(path))  # for debugging
    path_pathlib = Path(path)
    if not path_pathlib.parent.exists():
        path_pathlib.parent.mkdir(exist_ok=False, parents=True)
        print(f"Note: The {path_pathlib.parent} directory was successfully created.")

    if not path_pathlib.exists():
        print(f"Output saved by creating file at {path_pathlib}.")
        # TODO: Call this later maybe?

    if path_pathlib.exists():
        print(f"Output saved by overwring previous file at {path_pathlib}.")
        # TODO: Call this later maybe?

    return path_pathlib


@magics_class
class CaptureMagic(Magics):
    @magic_arguments.magic_arguments()  ################### TEXT
    @magic_arguments.argument(
        "--path",
        "-p",
        default=None,
        help=("The path where the text will be saved to"),
    )
    @cell_magic
    def capture_text(self, line, cell):
        args = magic_arguments.parse_argstring(CaptureMagic.capture_text, line)
        paths_string = args.path.strip('"').split(" ")
        paths_pathlib = []
        for path_str in paths_string:
            path_pathlib = path_preprocessing(path_str)
            paths_pathlib.append(path_pathlib)

        # TODO: for capture_text, paths_string has only one element, so this would not be necessary here.
        # It's just for convenicene, as the other capture functions are implemented with the same loop.

        with capture_output(stdout=True, stderr=False, display=False) as result:
            self.shell.run_cell(cell)
            message = result.stdout

        if len(message) == 0:
            raise ValueError("No standard output (stdout) found!")
        print(message)
        dest = paths_pathlib[0]
        dest.write_text(message)


    @magic_arguments.magic_arguments()  ################### Code
    @magic_arguments.argument(
        "--path",
        "-p",
        default=None,
        help=("The path where the code will be saved to"),
    )
    @cell_magic
    def capture_code(self, line, cell):
        args = magic_arguments.parse_argstring(CaptureMagic.capture_code, line)
        paths_string = args.path.strip('"').split(" ")
        paths_pathlib = []
        for path_str in paths_string:
            path_pathlib = path_preprocessing(path_str)
            paths_pathlib.append(path_pathlib)

        # TODO: for capture_code, paths_string has only one element, so this would not be necessary here.
        # It's just for convenicene, as the other capture functions are implemented with the same loop.

        with capture_output(stdout=True, stderr=False, display=False) as result:
            self.shell.run_cell(cell)
#            message = result.stdout

        message = cell
        dest = paths_pathlib[0]
        dest.write_text(message)






    @magic_arguments.magic_arguments()  ################### IMAGE
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

        paths_string = args.path.strip('"').split(" ")
        paths_pathlib = []
        for path_str in paths_string:
            path_pathlib = path_preprocessing(path_str)
            paths_pathlib.append(path_pathlib)

        with capture_output(stdout=False, stderr=False, display=True) as result:
            self.shell.run_cell(cell)
        for output in result.outputs:
            display(output)
            data = output.data
            if "image/png" in data:
                path = paths_pathlib.pop(0)
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

    @magic_arguments.magic_arguments()  ################### Video
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

        paths_string = args.path.strip('"').split(" ") # TODO: Maybe also with path_preprocessing ?
        paths_pathlib = []
        for path_str in paths_string:
            path_pathlib = path_preprocessing(path_str)
            paths_pathlib.append(path_pathlib)

        with capture_output(stdout=False, stderr=False, display=True) as result:
            self.shell.run_cell(cell)
        for output in result.outputs:
            display(output)
            data = output.data
            # pprint(data) # for debugging

            if "text/html" in data:
                path = paths_pathlib.pop(0)
                if not path:
                    raise ValueError("Too few paths given!")
                video_object_html_string = data["text/html"]

                # Extract video source filename
                pattern = re.compile(r'video src="(.+?)"')
                match = pattern.search(video_object_html_string)

                if match:
                    video_dir = match.group(1)
                    dest = Path(path)
                    src = Path(video_dir)
                    dest.write_bytes(src.read_bytes())

                # Extract base64-encoded embedded video data 
                pattern = re.compile(r'data:video/mp4;base64,(.*)">')
                match = pattern.search(video_object_html_string)

                if match:
                    base64_string = match.group(1)

                    # Decode base64 string and save video file using pathlib
                    video_bytes = b64decode(base64_string)
                    assert isinstance(video_bytes, bytes)
                    dest = Path(path)
                    dest.write_bytes(video_bytes)

