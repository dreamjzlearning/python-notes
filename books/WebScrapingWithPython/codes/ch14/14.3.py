# 14.3.py
# Handling Redirection

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

CHROME_DRIVER_PATH = ChromeDriverManager().install()


def wait_for_load(driver):
    for _ in range(20):
        try:
            driver.find_element(By.TAG_NAME, "html")
        except StaleElementReferenceException:
            return
        time.sleep(0.5)

    print("Timing out after 10s")


chrome_options = Options().add_argument("--headless")
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=chrome_options)
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
wait_for_load(driver)

print(driver.page_source)

driver.close()
