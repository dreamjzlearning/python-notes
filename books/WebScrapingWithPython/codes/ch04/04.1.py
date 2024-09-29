"""
04.1.py
get html from server
"""

from urllib.request import urlopen

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
print(html.read())
