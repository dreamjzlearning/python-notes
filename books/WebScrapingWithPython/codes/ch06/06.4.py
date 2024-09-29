# 06.4.py
# Crawling Across the Internet

from urllib.request import urlopen
from urllib.parse import urlparse

from bs4 import BeautifulSoup

import random
import time

random.seed(time.time())


# Retrieve a list of all Internal links found on a page
def get_internal_links(bs, url):
    netloc = urlparse(url).netloc
    scheme = urlparse(url).scheme

    internal_links = set()
    for link in bs.find_all("a"):
        if "href" not in link.attrs:
            continue

        u = link.attrs["href"]
        parsed = urlparse(u)
        if parsed.netloc == "":
            l = f"{scheme}://{netloc}/{u.strip('/')}"
            internal_links.add(l)
        elif parsed.netloc == netloc:
            internal_links.add(u)

    return list(internal_links)


# Retrieves a list of all external links found on a page
def get_external_links(bs, url):
    netloc = urlparse(url).netloc

    extern_links = set()
    for link in bs.find_all("a"):
        if "href" not in link.attrs:
            continue

        u = link.attrs["href"]
        parsed = urlparse(u)
        if parsed.netloc != "" and parsed.netloc != netloc:
            extern_links.add(u)

    return list(extern_links)


def get_random_external_link(starting_page):
    bs = BeautifulSoup(urlopen(starting_page), "html.parser")
    external_links = get_external_links(bs, starting_page)
    if not len(external_links):
        print("No external links, look around the site for one")
        internal_links = get_internal_links(bs, starting_page)
        return get_random_external_link(random.choice(internal_links))
    else:
        return random.choice(external_links)


def follow_external_only(starting_page):
    external_link = get_random_external_link(starting_page)
    print(f"Random external link is: {external_link}")
    follow_external_only(external_link)


url = "https://www.oreilly.com/"

follow_external_only(url)
