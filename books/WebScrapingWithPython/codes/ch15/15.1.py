# 15.1.py
# Parsing JSON

import json
from urllib.request import urlopen


def get_country(ip_addr):
    res = urlopen("http://ip-api.com/json/" + ip_addr).read().decode("utf-8")
    res_json = json.loads(res)
    return res_json.get("countryCode")


print(get_country("50.78.253.58"))

json_str = """
{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],
 "arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},
 {"fruit":"pear"}]}
"""
json_obj = json.loads(json_str)

print(json_obj.get("arrayOfNums"))
print(json_obj.get("arrayOfFruits")[2])
