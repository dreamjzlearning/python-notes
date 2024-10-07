# 13.2.py
# Uploading Files

import requests

files = {"uploadFile": open("test.txt", "r")}

r = requests.post("http://pythonscraping.com/pages/files/processing2.php", files=files)

print(r.text)
