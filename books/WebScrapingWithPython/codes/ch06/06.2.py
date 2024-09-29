# 06.2.py
# Crawling the Entire Site

from urllib.request import urlopen

from bs4 import BeautifulSoup

import re

wiki_url_prefix = "http://en.wikipedia.org{}"


pages = set()


def get_links(page_url):
    html = urlopen(wiki_url_prefix.format(page_url))
    bs = BeautifulSoup(html, "html.parser")

    link_reg = r"^(/wiki/)"
    for link in bs.find_all("a", href=re.compile(link_reg)):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                # add new page
                new_page = link.attrs["href"]
                print(new_page)
                pages.add(new_page)

                get_links(new_page)


# start from home page
get_links("")
