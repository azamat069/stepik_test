from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://suninjuly.github.io/math.html')
    x_element = driver.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.CLASS_NAME, 'btn.btn-default').click()
finally:
    time.sleep(10)
    driver.quit()
