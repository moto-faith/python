import pytesseract
from PIL import Image
image = Image.open('image.png')
print(pytesseract.image_to_string(image))