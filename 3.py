from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://suninjuly.github.io/huge_form.html')
    input = driver.find_elements(By.TAG_NAME, 'input')
    for i in input:
        i.send_keys('input')
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(10)
    driver.quit()