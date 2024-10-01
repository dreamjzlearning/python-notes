# 09.4.py
# Save HTML table as CSV

import csv

from urllib.request import urlopen
from bs4 import BeautifulSoup

bs = BeautifulSoup(
    urlopen(
        "https://en.wikipedia.org/wiki/List_of_countries_with_McDonald%27s_restaurants"
    ),
    "html.parser",
)

table = bs.find("table", {"class": "wikitable"})
rows = table.find_all("tr")
csv_file = open("countries.csv", "w+", encoding="UTF-8")
writer = csv.writer(csv_file)
try:
    for row in rows:
        csv_row = []
        for cell in row.find_all(["td", "th"]):
            csv_row.append(cell.get_text().strip())
        writer.writerow(csv_row)
finally:
    csv_file.close()
