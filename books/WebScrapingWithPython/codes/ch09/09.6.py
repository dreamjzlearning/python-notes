# 09.6.py
# Storing data into MySQL

import pymysql
import re
import random
import time

from urllib.request import urlopen
from bs4 import BeautifulSoup

random.seed(time.time())

conn = pymysql.connect(
    host="xxx",
    port=4567,
    user="xxx",
    password="xxx",
    charset="utf8",
)

cur = conn.cursor()
cur.execute("USE scraping")


def store(title, content):
    cur.execute(
        'INSERT INTO pages (title, content) VALUES ("%s", "%s")', (title, content)
    )
    cur.connection.commit()


def get_links(article_url):
    bs = BeautifulSoup(urlopen("http://en.wikipedia.org" + article_url), "html.parser")

    title = bs.find("h1").get_text()
    content = bs.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)

    return bs.find("div", {"id": "bodyContent"}).find_all(
        "a", href=re.compile(r"(/wiki/)((?!:).)*$")
    )


links = get_links("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        new_article = links[random.randint(0, len(links) - 1)].attrs["href"]
        print(new_article)
        links = get_links(new_article)
finally:
    cur.close()
    conn.close()
