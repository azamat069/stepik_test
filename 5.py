from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://suninjuly.github.io/registration2.html')
    driver.find_element(By.XPATH, '//input[@placeholder="Input your first name"]').send_keys('Azamat')
    driver.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys('Tester')
    driver.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys('tester@gmail.com')
    driver.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]').send_keys('+79999999999')
    driver.find_element(By.XPATH, '//input[@placeholder="Input your address:"]').send_keys('Moscow')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

finally:
    time.sleep(10)
    driver.quit()
