from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://suninjuly.github.io/file_input.html')
    driver.find_element(By.XPATH, '//input[@name="firstname"]').send_keys('Azamat')
    driver.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('Tester')
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('tester@google.com')
    driver.find_element(By.XPATH, '//input[@name="file"]').send_keys('/Users/azamatabdurasidov/PycharmProjects/stepik_course/file.txt')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

finally:
    time.sleep(5)
    driver.quit()