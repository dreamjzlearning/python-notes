# 07.1.py
# Dealing with Different Website Layouts

from urllib.request import urlopen
from bs4 import BeautifulSoup


class Content:
    """
    Common base class for all articles
    """

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print(f"Title: {self.title}")
        print(f"URL: {self.url}")
        print(f"Body: {self.body}")


class Website:
    """
    Contains information about website structure
    """

    def __init__(self, name, url, title_tag, body_tag):
        self.url = url
        self.name = name
        self.title_tag = title_tag
        self.body_tag = body_tag


class Crawler:
    @classmethod
    def get_page(cls, url):
        try:
            html = urlopen(url)
        except Exception:
            return None
        return BeautifulSoup(html, "html.parser")

    @classmethod
    def safe_get(cls, bs, selector):
        """
        Gets content from a bs object and a selector
        """
        selected_elements = bs.select(selector)
        if selected_elements is not None and len(selected_elements) > 0:
            return "\n".join([elem.get_text() for elem in selected_elements])
        return ""

    @classmethod
    def get_content(cls, website, path):
        """
        Extract content from a given page URL
        """
        url = website.url + path
        bs = Crawler.get_page(url)
        if bs is not None:
            title = Crawler.safe_get(bs, website.title_tag)
            body = Crawler.safe_get(bs, website.body_tag)
            return Content(url, title, body)
        return Content(url, "", "")


siteData = [
    ["O'Reilly", "https://www.oreilly.com", "h1", "div.title-description"],
    ["Reuters", "https://www.reuters.com", "h1", "div.ArticleBodyWrapper"],
    ["Brookings", "https://www.brookings.edu", "h1", "div.post-body"],
    ["CNN", "https://www.cnn.com", "h1", "div.article__content"],
]

websites = []
for name, url, title, body in siteData:
    websites.append(Website(name, url, title, body))

Crawler.get_content(
    websites[0], "/library/view/web-scraping-with/9781491910283"
).print()
Crawler.get_content(websites[1], "/article/us-usa-epa-pruitt-idUSKBN19W2D0").print()
Crawler.get_content(
    websites[2],
    "/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/",
).print()
Crawler.get_content(
    websites[3], "/2023/04/03/investing/dogecoin-elon-musk-twitter/index.html"
).print()
