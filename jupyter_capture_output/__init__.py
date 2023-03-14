from .co_cellmagic import CaptureMagic
from IPython import get_ipython  # register cell magic
import importlib.metadata

__version__: str = importlib.metadata.version(__name__)

print(f"Jupyter Capture Output v{__version__}")

try:
    ipy = get_ipython()
    ipy.register_magics(CaptureMagic)

except AttributeError:
    print("Can not load CaptureMagic because this is not a notebook")