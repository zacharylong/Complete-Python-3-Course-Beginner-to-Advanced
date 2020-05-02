import requests
from io import BytesIO
from PIL import Image

r = requests.get('https://wallpaperaccess.com/full/30005.jpg')
print('Status:', r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./image." + image.format


try:
    image.save(path, image.format)
except IOError:
    print('Cannot save image.')