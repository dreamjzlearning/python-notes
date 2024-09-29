"""
04.3.py
connect reliably and handling exception
"""

from urllib.request import urlopen
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        # if html is NONE, throw AttributeError
        bs = BeautifulSoup(html.read(), "html.parser")
        # if tag is NONE AttributeError
        title = bs.body.h1
    except AttributeError as e:
        return None

    return title


url = "http://www.pythonscraping.com/pages/page1.html"
title = getTitle(url)
if title == None:
    print("Title could not be found")
else:
    print(title)
