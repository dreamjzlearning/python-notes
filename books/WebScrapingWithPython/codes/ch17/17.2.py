# 17.2.py
# Handle Cookies by JavaScript

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome driver installation path
CHROME_DRIVER_PATH = ChromeDriverManager().install()

chrome_options = Options()
# headless mode runs chrome without visible UI
chrome_options.add_argument("--headless")

# Open http://pythonscraping.com and get the cookies

# start chrome and open page
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=chrome_options)

driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)

print("Driver1")
saved_cookies = driver.get_cookies()
print(saved_cookies)

# Open http://pythonscraping.com
# Delete and rewrite the cookie

driver2 = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=chrome_options)

driver2.get("http://pythonscraping.com")

print("Driver2")
print(driver2.get_cookies())
driver2.delete_all_cookies()
for cookie in saved_cookies:
    driver2.add_cookie(cookie)

print("Driver2 edited cookies")
print(driver2.get_cookies())

driver2.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print("Driver2 new cookies")
print(driver2.get_cookies())
