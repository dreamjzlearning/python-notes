# 10.4.py
# Reading .docx

from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

data = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
word_file = BytesIO(data)
doc = ZipFile(word_file)
xml_content = doc.read("word/document.xml")

word_obj = BeautifulSoup(xml_content.decode("utf-8"), "xml")
text = word_obj.find_all("w:t")

for t in text:
    style = t.parent.parent.find("w:pStyle")
    if style is not None and style["w:val"] == "Title":
        print(f"Title is: {t.text}")
    else:
        print(t.text)
