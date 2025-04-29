# 18.3.py
# Testing with Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CHROME_DRIVER_PATH = ChromeDriverManager().install()

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=chrome_options)

driver.get("http://en.wikipedia.org/wiki/Monty_Python")

assert "Monty Python" in driver.title

driver.close()
