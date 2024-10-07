# 12.1.py
# Summarizing Data

import re, string
from urllib.request import urlopen
from collections import Counter


def replace_newlines(text):
    return text.replace("\n", " ")


def make_lowercase(text):
    return text.lower()


def split_sentences(text):
    return [s.strip() for s in text.split(". ")]


puncts = [re.escape(c) for c in string.punctuation]
puncts_re = re.compile("|".join(puncts))


def remove_punctuation(text):
    return re.sub(puncts_re, "", text)


content = str(
    urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), "utf-8"
)

text_ops = [replace_newlines, split_sentences, make_lowercase, remove_punctuation]

cleaned = content
for op in text_ops:
    if type(cleaned) == list:
        cleaned = [op(c) for c in cleaned]
    else:
        cleaned = op(cleaned)

# print(cleaned)


def get_ngrams(text, n):
    text = text.split(" ")
    return [" ".join(text[i : i + n]) for i in range(len(text) - n + 1)]


def count_ngrams_from_sentences(sentences, n):
    counts = Counter()
    for sentence in sentences:
        counts.update(get_ngrams(sentence, n))
    return counts


counts = count_ngrams_from_sentences(cleaned, 2)
# print(counts.most_common())

common_words = [
    "the",
    "be",
    "and",
    "of",
    "a",
    "in",
    "to",
    "have",
    "it",
    "i",
    "that",
    "for",
    "you",
    "he",
    "with",
    "on",
    "do",
    "say",
    "this",
    "they",
    "is",
    "an",
    "at",
    "but",
    "we",
    "his",
    "from",
    "that",
    "not",
    "by",
    "she",
    "or",
    "as",
    "what",
    "go",
    "their",
    "can",
    "who",
    "get",
    "if",
    "would",
    "her",
    "all",
    "my",
    "make",
    "about",
    "know",
    "will",
    "as",
    "up",
    "one",
    "time",
    "has",
    "been",
    "there",
    "year",
    "so",
    "think",
    "when",
    "which",
    "them",
    "some",
    "me",
    "people",
    "take",
    "out",
    "into",
    "just",
    "see",
    "him",
    "your",
    "come",
    "could",
    "now",
    "than",
    "like",
    "other",
    "how",
    "then",
    "its",
    "our",
    "two",
    "more",
    "these",
    "want",
    "way",
    "look",
    "first",
    "also",
    "new",
    "because",
    "day",
    "more",
    "use",
    "no",
    "man",
    "find",
    "here",
    "thing",
    "give",
    "many",
    "well",
]


def is_common(ngram):
    return any([w in common_words for w in ngram.split(" ")])


def filter_common(counts):
    return Counter({key: val for key, val in counts.items() if not is_common(key)})


print(filter_common(counts).most_common())
