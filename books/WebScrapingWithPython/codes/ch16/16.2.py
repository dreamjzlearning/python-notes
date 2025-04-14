# 16.2.py
# Tesseract

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"D:\Apps\tesseract"

print(pytesseract.image_to_string(Image.open("ocr_tst.png")))
