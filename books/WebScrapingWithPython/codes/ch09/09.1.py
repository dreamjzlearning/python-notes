# 09.1.py
# Download python logo

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

bs = BeautifulSoup(urlopen("http://www.pythonscraping.com/"), "html.parser")
img_url = bs.find("img", {"alt": "python-logo"})["src"]
urlretrieve(img_url, "logo.jpg")
