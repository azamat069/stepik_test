from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def find(loc):
    return driver.find_element(By.XPATH, loc)

def scroll(var):
    driver.execute_script("return arguments[0].scrollIntoView(true);", find(var))

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]' ), '$100'))
    find('//button[@id="book"]').click()
    scroll('//span[@id="input_value"]')
    num = find('//span[@id="input_value"]').text
    result = calc(num)
    find('//input[@id="answer"]').send_keys(result)
    find('//button[@id="solve"]').click()

finally:
    time.sleep(5)
    driver.quit()