# 17.3.py
# Avoiding Honeypots

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Get chrome installation path
CHROME_DRIVER_PATH = ChromeDriverManager().install()

# Chrome Options
chrome_options = Options()
# Headless mode
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=chrome_options)

driver.get("http://pythonscraping.com/pages/itsatrap.html")
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    if not link.is_displayed():
        print(f'The link {link.get_attribute("href")} is a trap')

fields = driver.find_elements(By.TAG_NAME, "input")
for field in fields:
    if not field.is_displayed():
        print(f'Do not change value of {field.get_attribute("name")}')
