# jupyter-caputure-output
A cell magic that captures jupyter cell output

## Install
Requires Python >=3.7
```py
pip install jupyter_capture_output
```

## Example

```py
import jupyter_capture_output
import matplotlib.pyplot as plt
```

```py
%%capture_img --path "foo.png bar.png"
plt.plot([1,2],[10,20])
plt.show()
plt.plot([3,4],[-10,-20])
plt.show()
```

```py
%%capture_img  --path "foo.jpg bar.jpg" --compression 50
plt.plot([1,2],[10,20], color = "r")
plt.show()
plt.plot([3,4],[-10,-20],color = "r")
plt.show()
```

## Wishlist
* JupyterLite version of this.
```py
from pathlib import Path

path = Path.cwd() / "foo.txt"
path.write_text("Hello World")
```
is not working yet, but might be soon: https://github.com/jupyterlite/jupyterlite/pull/655

* `%%capture_text`  ->  to .txt file with text output
* `%%capture_svg` ->  to .svg file with svg vectorgraphic outout
* `%%capture_video` -> to .mp4 file with the video output
* `%%capture_numpy_array` -> to .np file with array in it
* `%%capture_csv` -> tc .csv with datapoints in it
* `%%capture_dataframe` -> to .pkl file

## Changelog

### 0.0.4

Add Text and Video capture cell magic
update example

### 0.0.3

Setup automatic release action.

### 0.0.2

Update example

### 0.0.1

Initial release
