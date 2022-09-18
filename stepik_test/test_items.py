import time
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_language(browser):
    browser.get(link)
    button = browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    button_text = button.text
    assert button_text == 'Añadir al carrito', 'Wrong language'
    time.sleep(10)
