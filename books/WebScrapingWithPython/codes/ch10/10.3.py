# 10.3.py
# Reading PDF

from urllib.request import urlretrieve
from pypdf import PdfReader

file_name = "chapter1.pdf"

urlretrieve("http://pythonscraping.com/pages/warandpeace/chapter1.pdf", file_name)

reader = PdfReader(file_name)

for page in reader.pages:
    print(page.extract_text())
