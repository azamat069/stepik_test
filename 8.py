from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://suninjuly.github.io/selects1.html')
    num1 = driver.find_element(By.ID, 'num1').text
    num2 = driver.find_element(By.ID, 'num2').text
    sum = int(num1)+int(num2)
    select = Select(driver.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(sum))
    driver.find_element(By.CLASS_NAME, 'btn.btn-default').click()

finally:
    time.sleep(10)
    driver.quit()