# 13.4.py
# HTTP basic access authentication

import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("a", "password")
r = requests.post(url="https://pythonscraping.com/pages/auth/login.php", auth=auth)
print(r.text)
