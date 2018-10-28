# Create a shape
```python
import module.draw

point1 = (0, 0)
point2 = (1, 0)
point3 = (1, 1)
point4 = (0, 1)
color = (0, 0, 0) # rgb max (255, 255, 255)

module.draw.Objects.rect(point1, point2, point3, point4, color) # draw a rectangle
module.draw.Objects.tri(point1, point2, point3, color) # draw a triangle
```

# Write a text
```python
import module.draw
x = 0
y = 0
module.draw.Text.write("asdf", x, y)
```

# Render an image
```python
from module.images import Texture

filename = "../res/test.png"
posX = 0
posY = 0

myImage = Texture(filename)
myImage.render(posX, posY)
```

## Change size of image
```python
from module.images import Texture
filename = "../res/test.png"
newWidth = 10
newHeight = 10
myImage = Texture(filename)
myImage.setSize(newWidth, newHeight)
```