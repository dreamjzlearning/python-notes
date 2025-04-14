# 14.2.py
# Waiting load

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CHROME_DRIVER_PATH = ChromeDriverManager().install()

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=chrome_options)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loadedButton"))
    )
except Exception as e:
    print(f"failed to load pages: {e}")
else:
    print(driver.find_element(By.ID, "content").text)
finally:
    driver.close()
