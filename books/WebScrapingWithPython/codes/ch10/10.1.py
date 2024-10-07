# 10.1.py

from urllib.request import urlopen

text = urlopen("https://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")

# define the string to be utf-8
print(str(text.read(), "utf-8"))
