import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


link = "https://stage7.cofi-dev.ru"
login = "jksdfdasfsfsdf@mailinator.com"
password = "Password1"



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_app_create(driver):
    driver.get(link)
    driver.maximize_window()
    driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/header/div/div/nav/div/div/div').click()
    time.sleep(2)
    driver.refresh()

    #Авторизация
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/form/label[1]/input').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/form/label[2]/input').send_keys(password)
    driver.find_element(By.CLASS_NAME, 'button').click()

    #Переход на страницу создания заявки
    driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/header/div/div/nav/div/a[4]/div').click()
    driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/main/div/div/div[1]/button').click()

    #Создание заявки
    driver.find_element(By.XPATH, '//*[@id="description"]').click()
    lib_file = 'C:/Co_Fi_automated/auto_tests/application_create/lib.txt'
    application_name = open(lib_file).read().splitlines()
    driver.find_element(By.XPATH, '//*[@id="name"]/div/div/input').send_keys(application_name)
    time.sleep(5)













