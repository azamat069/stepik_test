import self as self
from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime as DT
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

random_email = (''.join(random.choice(string.ascii_lowercase) for i in range(12)))
print(random_email)
print(random_email)

