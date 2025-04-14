# 17.1.py
# Adjust Headers

import requests
from bs4 import BeautifulSoup

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

url = "https://www.whatismybrowser.com/"

req = session.get(url, headers=headers)

bs = BeautifulSoup(req.text, "html.parser")
print(bs.find("div", {"class": "string-major"}).find("a").get_text())
