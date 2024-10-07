# 13.1.py
# Submitting a Basic Form

import requests


url = "https://pythonscraping.com/pages/files/processing.php"
params = {"firstname": "A", "lastname": "B"}

r = requests.post(url, data=params)

print(r.text)
