def resize_image(image, width, height):
    from PIL import Image
    return image.resize((width, height), Image.ANTIALIAS)

## load file and call function
from PIL import Image
image = Image.open('big-elephant.jpg')
image = resize_image(image, 100, 100)
image.save('image_resized.jpg')
