from PIL import Image
import cv2
import pyTesseract

img = Image.open(r"Screenshot 2023-07-03 191242.png")
img1 = cv2.imread(r'Screenshot 2023-07-03 191242.png')

left = 800
top = 42
right = 1115
bottom = 100

crped_img = img.crop((left, top, right, bottom))
crped_img.save(r"resized.png")
print(pyTesseract.image_to_string(Image.open(r"resized.png")))
