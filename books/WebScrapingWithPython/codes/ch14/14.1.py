# 14.1.py
# Loading page with Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome driver installation path
CHROME_DRIVER_PATH = ChromeDriverManager().install()

chrome_options = Options()
# headless mode runs chrome without visible UI
chrome_options.add_argument("--headless")

# start chrome and open page
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=chrome_options)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")

# waiting for page loaded
time.sleep(3)

print(driver.find_element(By.ID, "content").text)

driver.close()
