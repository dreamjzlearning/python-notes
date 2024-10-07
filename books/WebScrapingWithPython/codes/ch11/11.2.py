# 11.2.py
# Breaking text into n-grams


def get_ngrams(text, n):
    text = text.split(" ")
    return [text[i : i + n] for i in range(len(text) - n + 1)]


ret = get_ngrams("web scraping with python", 2)
print(ret)
