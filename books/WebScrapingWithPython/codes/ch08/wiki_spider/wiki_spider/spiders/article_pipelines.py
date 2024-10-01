# ch08\wiki_spider\wiki_spider\spiders\article_pipelines.py

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wiki_spider.items import Article


class ArticleSpider(CrawlSpider):
    name = "article_pipelines"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Benevolent_dictator_for_life"]
    rules = [
        Rule(  # only article links allowed
            LinkExtractor(allow=r"(/wiki/)((?!:).)*$"),
            callback="parse_items",
            follow=True,
        )
    ]

    def parse_items(self, response):
        article = Article()
        article["url"] = response.url
        article["title"] = response.css("span.mw-page-title-main::text").extract_first()
        article["text"] = response.xpath(
            '//div[@id="mw-content-text"]//text()'
        ).extract()
        article["last_updated"] = response.css(
            "li#footer-info-lastmod::text"
        ).extract_first()

        return article