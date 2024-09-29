"""
05.1.py
find tags
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), "html.parser")

# find_all(tagName, tagAttributes)
name_list = bs.find_all("span", {"class": "green"})
for name in name_list:
    print(name.get_text())  # get content of tag
