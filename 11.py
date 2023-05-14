from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://suninjuly.github.io/alert_accept.html')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.switch_to.alert.accept()
    num = driver.find_element(By.XPATH, '//span[@id="input_value"]').text
    result = calc(num)
    driver.find_element(By.XPATH, '//input[@id="answer"]').send_keys(result)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

finally:
    time.sleep(5)
    driver.quit()