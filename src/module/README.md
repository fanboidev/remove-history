# Create a shape
```python
import module.draw

point1 = (0, 0)
point2 = (1, 0)
point3 = (1, 1)
point4 = (0, 1)

module.draw.Objects.rect(point1, point2, point3, point4) # draw a rectangle
module.draw.Objects.tri(point1, point2, point3) # draw a triangle
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
sizeX = 5
sizeY = 5

myImage = Texture(filename)
myImage.render(posX, posY, sizeX, sizeY)
```