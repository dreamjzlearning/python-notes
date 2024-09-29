# 06.3.py
# Collecting data across an entire site

from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

wiki_base_url = "http://en.wikipedia.org{}"

pages = set()


def get_links(page_url):
    html = urlopen(wiki_base_url.format(page_url))
    bs = BeautifulSoup(html, "html.parser")
    try:
        print(bs.h1.get_text())
        print(bs.find(id="mw-content-text").find_all("p")[0])
        print(bs.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("This page is missing something, continuing")

    link_reg = r"^(/wiki/)"
    for link in bs.find_all("a", href=re.compile(link_reg)):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                new_page = link.attrs["href"]
                print("-" * 20)
                print(new_page)
                pages.add(new_page)
                get_links(new_page)


get_links("")
