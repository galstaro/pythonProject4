from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep

class category_page:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def products(self):
        products_elements=self.driver.find_elements(By.CSS_SELECTOR,".categoryRight>ul>li")
        return products_elements

    def click_product(self):
        random.choice(self.products()).click()

