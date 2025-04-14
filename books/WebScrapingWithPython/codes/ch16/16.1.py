# 16.1.py
# Pillow

from PIL import Image, ImageFilter

img = Image.open("test.jpeg")

blurry_img = img.filter(ImageFilter.GaussianBlur)
blurry_img.save("blur.jpeg")
blurry_img.show()
