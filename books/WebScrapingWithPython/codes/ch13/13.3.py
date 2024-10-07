# 13.3.py
# Login

import requests

params = {"username": "Ryan", "password": "password"}

r = requests.post("https://pythonscraping.com/pages/cookies/welcome.php", data=params)

print(r.text)

print("Cookie is set to:")
print(r.cookies.get_dict())
print("Going to profile page...")

r = requests.get(
    "https://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies
)

print(r.text)

session = requests.Session()

params = {
    "username": "A",
    "password": "password"
}