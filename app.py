from PIL import Image

with Image.open('square.png') as image:
    print(image.format, image.size, image.mode)
