# 07.2.py
# Crawling Sites Through Search

from urllib.request import urlopen

from bs4 import BeautifulSoup


class Content:
    """
    Common base class for articles
    """

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Flexible printing function controls output
        """
        print("New article found topic: {}".format(self.topic))
        print("URL: {}".format(self.url))
        print("Title: {}".format(self.title))
        print("Body:\n {}".format(self.body))


class Website:
    """
    Contains information about website structure
    """

    def __init__(
        self,
        name,
        url,
        search_url,
        result_list,
        result_url,
        abs_url,
        title_tag,
        body_tag,
    ):
        self.name = name
        self.url = url
        self.search_url = search_url
        self.result_list = result_list
        self.result_url = result_url
        self.abs_url = abs_url
        self.title_tag = title_tag
        self.body_tag = body_tag


class Crawler:
    def __init__(self, website):
        self.site = website
        self.found = {}

    @classmethod
    def get_page(cls, url):
        try:
            html = urlopen(url)
        except Exception:
            return None
        return BeautifulSoup(html, "html.parser")

    @classmethod
    def safe_get(cls, bs, selector):
        selected_elements = bs.select(selector)
        if selected_elements is not None and len(selected_elements) > 0:
            return "\n".join([elem.get_text() for elem in selected_elements])
        return ""

    def get_content(self, topic, url):
        """
        Extract content from a given page URL
        """
        bs = Crawler.get_page(url)
        if bs is not None:
            title = Crawler.safe_get(bs, self.site.title_tag)
            body = Crawler.safe_get(bs, self.site.body_tag)
            return Content(topic, url, title, body)
        return Content(topic, url, "", "")

    def search(self, topic):
        """
        Searches a given website for a given topic and records all pages found
        """
        bs = Crawler.get_page(self.site.search_url + topic)
        results = bs.select(self.site.result_list)

        for result in results:
            url = result.select(self.site.result_url)[0].attrs["href"]
            # check to see whether it's a relative or an absolute URL
            url = url if self.site.abs_url else self.site.url + url
            if url not in self.found:
                self.found[url] = self.get_content(topic, url)
            self.found[url].print()


siteData = [
    [
        "Reuters",
        "https://reuters.com",
        "https://www.reuters.com/site-search/?query=",
        "div[class*=search-results__list]",
        "header.heder a",
        False,
        "h1",
        "div[class*=article-body__wrapper]",
    ],
    [
        "Brookings",
        "https://www.brookings.edu",
        "https://www.brookings.edu/search/?s=",
        "div.article-info",
        "h4.title a",
        True,
        "h1",
        "div.core-block",
    ],
]

sites = []

for name, url, search, rListing, rUrl, absUrl, tt, bt in siteData:
    sites.append(Website(name, url, search, rListing, rUrl, absUrl, tt, bt))

crawlers = [Crawler(site) for site in sites]
topics = ["python", "data%20science"]

for topic in topics:
    for crawler in crawlers:
        crawler.search(topic)
