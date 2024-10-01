# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from datetime import datetime
from wiki_spider.items import Article
from string import whitespace


class WikiSpiderPipeline:
    def process_item(self, article, spider):
        date_str = article["last_updated"]
        date_str = date_str.replace("This page was last edited on ", "").strip()
        date_str = datetime.strptime(date_str, "%d %B %Y, at %H:%M")
        article["last_updated"] = date_str

        text = [line for line in article["text"] if line not in whitespace]
        article["text"] = "".join(text)

        return article
