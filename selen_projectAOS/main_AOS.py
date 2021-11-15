from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import locale
from home_page_class import home_page

service1 = Service(r"C:\chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service1)
driver.get("https://advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
home=home_page(driver)
home.user_emoji_click()
home.enter_username()
home.enter_password()
home.sign_in_click()
home.user_emoji_click()
home.click_sign_out()
sleep(3)
driver.close()