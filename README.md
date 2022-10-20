# jupyter-caputure-output
A cell magic that captures jupyter cell output


[![JupyterLight](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://octoframes.github.io/jupyter_capture_output/)  

## Install
Requires Python >=3.8
```py
pip install jupyter_capture_output
```


## Example

https://user-images.githubusercontent.com/44469195/184531492-6bc34ed9-3640-447b-b09e-767d01ecf3da.mov


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
* `%%capture_video` -> to .mp4 file with the video output

## Wishlist

* `%%capture_svg` ->  to .svg file with svg vectorgraphic outout
* `%%capture_numpy_array` -> to .np file with array 
* `%%capture_csv` -> to .csv with datapoints 
* `%%capture_gif` -> to .gif with animation
* `%%capture_auto`-> automatically detects what output there is to capture

## Changelog

### 0.0.8 (work in progress)

### 0.0.7 

* Add relative path support and automatically create paths if they don't exist yet.

Add some experimental magic, but this will likely be removed in future versions:
* * `experimental_capture_video_first_last` captures video and extracts first and last frame from it. Useful for post-processing of videos in other video editors. Needs ffmpeg installed

* `experimental_video_thumbnail` extracts video from the Jupyter cell output, and replaces it with an image thumbnail of the video -> useful for Version control. Needs matplotlib and ffmpeg installed
### 0.0.6

better regex in capture video
change example images to dogs

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
