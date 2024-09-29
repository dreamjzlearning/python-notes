"""
05.3.py
Regular Expressions
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, "html.parser")

# matches regexp ../img/gifts/img.*\.jpg
images = bs.find_all("img", {"src": re.compile(r"../img/gifts/img.*\.jpg")})

for image in images:
    # access attributes
    print(image.attrs)
    # using attr name
    print(image.attrs["src"])
    # simple way
    print(image["src"])
