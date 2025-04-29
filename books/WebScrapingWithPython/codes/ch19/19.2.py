# 19.2.py
# Multithreaded Crawling

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, random, threading, time


# Recursively find links on a wikipedia page,
# then follow a random link, with artificial 5 sec delay
def scrape_article(thread_name, path):
    time.sleep(5)

    print(f"{thread_name}: Scraping {path}")
    html = urlopen("http://en.wikipedia.org{}".format(path))
    bs = BeautifulSoup(html, "html.parser")

    links = bs.find("div", {"id": "bodyContent"}).find_all(
        "a", href=re.compile("^(/wiki/)((?!:).)*$")
    )
    if len(links) > 0:
        new_article = links[random.randint(0, len(links) - 1)].attrs["href"]
        scrape_article(thread_name, new_article)


threads = [
    threading.Thread(target=scrape_article, args=("T-1", "/wiki/Kevin_Bacon")),
    threading.Thread(target=scrape_article, args=("T-2", "/wiki/Monty_Python")),
]

[t.start() for t in threads]
[t.join() for t in threads]
