# ch08\wiki_spider\wiki_spider\spiders\article_more_rules.py

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ArticleSpider(CrawlSpider):
    name = "articles"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Benevolent_dictator_for_life"]
    rules = [
        Rule(  # only article links allowed
            LinkExtractor(allow=r"(/wiki/)((?!:).)*$"),
            callback="parse_items",
            follow=True,
            cb_kwargs={"is_article": True},
        ),
        Rule(  # all links
            LinkExtractor(allow=".*"),
            callback="parse_items",
            cb_kwargs={"is_article": False},
        ),
    ]

    def parse_items(self, response, is_article):
        title = response.css("span.mw-page-title-main::text").extract_first()
        if is_article:
            url = response.url
            text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
            last_updated = response.css("li#footer-info-lastmod::text").extract_first()
            last_updated = last_updated.replace("'This page was last edited on ", "")
            print(f"URL is: {url}")
            print(f"Title is: {title}")
            print(f"Text is: {text}")
            print(f"Last updated: {last_updated}")
        else:
            print(f"{title} is not an article. URL: {response.url} ")
