# 06.1.py
# article links crawler

from urllib.request import urlopen

from bs4 import BeautifulSoup

import re
import random
import time

random.seed(time.time())

wiki_url = "http://en.wikipedia.org{}"


def get_links(article_url):
    html = urlopen(wiki_url.format(article_url))

    bs = BeautifulSoup(html, "html.parser")
    article_reg = r"^(/wiki/)((?!:).)*$"
    return bs.find("div", {"id": "bodyContent"}).find_all(
        "a", href=re.compile(article_reg)
    )


links = get_links("/wiki/Kevin_Bacon")
while len(links) > 0:
    new_article = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(new_article)
    links = get_links(new_article)
