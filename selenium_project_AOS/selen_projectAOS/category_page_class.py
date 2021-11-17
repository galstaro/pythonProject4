from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep
from sheet import AOS_Sheet


class category_page:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
        self.sheet = AOS_Sheet()

    def products(self,test_number,product_number):
        products_element=self.driver.find_element(By.ID,f"{self.sheet.get_Product_ID(test_number,product_number)}")
        return products_element

    def click_product(self,test_number,product_number):
        self.products(test_number,product_number).click()

    def category_title(self):
        text = self.driver.find_element(By.CLASS_NAME, "categoryTitle")
        return text.text

