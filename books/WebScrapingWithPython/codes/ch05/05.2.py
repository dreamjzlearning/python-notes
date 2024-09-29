"""
05.2.py
children and descendants
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html.read(), "html.parser")


# get children
print("\033[31mChildren:\033[0m")
for child in bs.find("table", {"id": "giftList"}).children:
    print(child)

# get siblings
print("\033[31mSiblings:\033[0m")
# next_siblings return all siblings of an object without the object itself
for sibling in bs.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

# get parents
# parent() and parents()
print(
    bs.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()
)
