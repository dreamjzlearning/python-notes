"""
05.4.py
Lambda Expressions
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


# lambda expression
squares = lambda n: n**2
print(squares(3))

url = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(url)
bs = BeautifulSoup(html, "html.parser")

# find tags that have 2 attrs
tags = bs.find_all(lambda tag: len(tag.attrs) == 2)
print(tags)
