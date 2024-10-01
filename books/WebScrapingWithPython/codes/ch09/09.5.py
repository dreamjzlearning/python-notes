# 09.5.py
# Connecting to MysQL

import pymysql

conn = pymysql.connect(host="xxx", port=4567, user="xxx", password="xxx", db="scraping")

cur = conn.cursor()
cur.execute("SELECT * FROM pages WHERE id=1")

print(cur.fetchone())

cur.close()
conn.close()
