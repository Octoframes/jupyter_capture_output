# jupyter-caputure-output
A cell magic that captures jupyter cell output

[![JupyterLight](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://kolibril13.github.io/jupyter-capture-output/)  

## Install
Requires Python >=3.8
```py
pip install jupyter_capture_output
```

## Example

```py
import jupyter_capture_output
```

```py 
%%capture_text --path "foo.txt"
print("Hello World")
```

```py
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



Implemented
* `%%capture_text`  ->  to .txt file with text output
* `%%capture_img` -> to .png or .jpg with image output
* `%%capture_video` (needs rework) -> to .mp4 file with the video output

## Wishlist

* `%%capture_svg` ->  to .svg file with svg vectorgraphic outout
* `%%capture_numpy_array` -> to .np file with array 
* `%%capture_csv` -> to .csv with datapoints 
* `%%capture_gif` -> to .gif with animation
* `%%capture_auto`-> automatically detects what output there is to capture

## Changelog


### 0.0.5

Remove debugging code
Add JupyterLiteDemo
### 0.0.4

Add Text and Video capture cell magic
update example

### 0.0.3

Setup automatic release action.

### 0.0.2

Update example

### 0.0.1

Initial release
