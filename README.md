# jupyter-caputure-output
A cell magic that captures jupyter cell output

## Install
Requires Python >=3.8
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

## Changelog

### 0.0.3

Setup automatic release action.

### 0.0.2

Update example

### 0.0.1

Initial release
