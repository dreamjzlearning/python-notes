# 07.3.py
# Crawling Sites Through Links

from urllib.request import urlopen
from bs4 import BeautifulSoup

import re


class Website:
    def __init__(self, name, url, pattern, abs_url, title_tag, body_tag):
        self.name = name
        self.url = url
        self.pattern = pattern
        self.abs_url = abs_url
        self.title_tag = title_tag
        self.body_tag = body_tag


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print(f"URL: {self.url}")
        print(f"Title: {self.title}")
        print(f"Body: \n{self.body}")


class Crawler:
    def __init__(self, site):
        self.site = site
        self.visited = {}

    @classmethod
    def get_page(cls, url):
        try:
            html = urlopen(url)
        except Exception as e:
            print(f"failed to open {url}: {e}")
            return None
        return BeautifulSoup(html, "html.parser")

    @classmethod
    def safe_get(cls, bs, selector):
        selected_elems = bs.select(selector)
        if selected_elems is not None and len(selected_elems) > 0:
            return "\n".join([elem.get_text() for elem in selected_elems])
        return ""

    def get_content(self, url):
        bs = Crawler.get_page(url)
        if bs is not None:
            title = Crawler.safe_get(bs, self.site.title_tag)
            body = Crawler.safe_get(bs, self.site.body_tag)
            return Content(url, title, body)
        return Content(url, "", "")

    def crawl(self):
        bs = Crawler.get_page(self.site.url)
        targets = bs.find_all("a", href=re.compile(self.site.pattern))
        for target in targets:
            url = target.attrs["href"]
            url = url if self.site.abs_url else f"{self.site.url}{url}"
            if url not in self.visited:
                self.visited[url] = self.get_content(url)
                self.visited[url].print()


brookings = Website(
    "Brookings",
    "https://brookings.edu",
    "\/(research|blog)\/",
    True,
    "h1",
    "div.post-body",
)

crawler = Crawler(brookings)
crawler.crawl()
