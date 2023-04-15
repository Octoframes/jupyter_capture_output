# jupyter-caputure-output
A cell magic that captures jupyter cell output


[![JupyterLight](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://octoframes.github.io/jupyter_capture_output/)  

## Install
Requires Python >=3.8
```py
pip install jupyter_capture_output
```


## Example

https://user-images.githubusercontent.com/44469195/199723257-ee428f53-d576-47be-93b9-d6ab98c46d8e.mov

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
* `%%capture_code`  ->  to .py file with cell content
* `%%capture_img` -> to .png or .jpg with image output
* `%%capture_video` -> to .mp4 file with the video output

## Use cases

* matplotlib, scipy, PIL , cv2, manim etc. have their own APIs to save images. With this package, one just have to learn one line of code and can use it to save all kind of image outputs made by different packages.

* When tweaking plots, one can use this cell magic to track the process, so to say a visual version control system.

* In context of Science, one can generate log files of experiments with this package. As the cell magic is always on the top of the cell, it's easy to see in which cells log files are generated and in which not.

* This can be used to create sheet cheats, e.g. this [math-functions-cheat-sheet](https://kolibril13.github.io/plywood-gallery-functions/) website was generated from a jupyter notebook using a derivative of this capture package.

* This package will also auto-generate the folder-tree of subdirectories for you.
## Changelog

### 0.0.11

* add support for embedded videos.

### 0.0.10

* use importlib.metadata
### 0.0.9

* support python 3.11
### 0.0.8 
*  Add `capture_code` magic. Because this is not cell output but cell content, it might be worth to think about renaming this project from `capture-output` to only `capture` or even `capture-content`.
* `remove experimental_capture_video_first_last` and `experimental_video_thumbnail` again. This package is not the right place for that.

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
