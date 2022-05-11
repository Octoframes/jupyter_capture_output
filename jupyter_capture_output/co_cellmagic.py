from io import BytesIO
from base64 import b64decode

from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import display
from IPython.utils.capture import capture_output
from PIL import Image


@magics_class
class CaptureMagic(Magics):
    @magic_arguments.magic_arguments()
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
