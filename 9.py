from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def scroll(var):
    driver.execute_script("return arguments[0].scrollIntoView(true);", var)

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://suninjuly.github.io/execute_script.html')
    num = driver.find_element(By.XPATH, '//span[@id="input_value"]').text
    result = calc(num)

    input = driver.find_element(By.XPATH, '//input[@id="answer"]')
    scroll(input)
    input.send_keys(result)

    checkbox = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
    scroll(checkbox)
    checkbox.click()

    radio = driver.find_element(By.XPATH, '//input[@id="robotsRule"]')
    scroll(radio)
    radio.click()

    button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    scroll(button)
    button.click()

finally:
    time.sleep(5)
    driver.quit()

