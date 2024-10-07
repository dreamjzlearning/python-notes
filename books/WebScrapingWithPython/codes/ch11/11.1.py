# 11.1.py
# Cleaning Text

from urllib.request import urlopen
from bs4 import BeautifulSoup

import re, string, unicodedata


def replace_newlines(text):
    return text.replace("\n", " ")


def make_lowercase(text):
    return text.lower()


def split_sentences(text):
    return [s.strip() for s in text.split(". ")]


CITATION_RE = re.compile(r"\[0-9*\]")


def strip_citations(text):
    return re.sub(CITATION_RE, "", text)


PARENTS_RE = re.compile(r"\([a-z A-Z \+\.,\-]{0,100}\)")


def remove_parentheses(text):
    return re.sub(PARENTS_RE, "", text)


DESCRIPTION_RE = re.compile(r"\n[a-z A-Z]*:")


def remove_descriptions(text):
    return re.sub(DESCRIPTION_RE, "", text)


PUNCTUATION_RE = re.compile("|".join([re.escape(c) for c in string.punctuation]))


def remove_punctuation(text):
    return re.sub(PUNCTUATION_RE, "", text)


def normalize(text):
    return unicodedata.normalize("NFKD", text)


text_operations = [
    strip_citations,
    remove_parentheses,
    remove_descriptions,
    replace_newlines,
    make_lowercase,
    split_sentences,
    remove_punctuation,
    normalize,
]

url = "http://en.wikipedia.org/wiki/Python_(programming_language)"
bs = BeautifulSoup(urlopen(url), "html.parser")

content = bs.find("div", {"id": "mw-content-text"}).find_all("p")
content = [p.get_text() for p in content]

cleaned = content
for op in text_operations:
    for i in range(len(cleaned)):
        c = cleaned[i]
        if type(c) == list:
            c = [op(s) for s in c]
        else:
            c = op(c)
        cleaned[i] = c

print(cleaned)
