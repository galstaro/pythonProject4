import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class product_page:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def add_to_cart(self):
        add_to_cart_element=self.driver.find_element(By.NAME,"save_to_cart")
        return add_to_cart_element

    def click_add_to_cart(self):
        self.add_to_cart().click()

    def quantity(self):
        return self.driver.find_element(By.NAME,"quantity")
    def change_quantity(self):
        self.quantity().click()
        self.quantity().send_keys(Keys.BACK_SPACE)
        quantity=random.randint(1,6)
        self.quantity().send_keys(f"{quantity}")
        return quantity

    def colors(self):
            rabbit=self.driver.find_elements(By.ID,"rabbit")
            if len(rabbit)!=0:
                return rabbit
            else:
                bunny = self.driver.find_elements(By.ID,"bunny")
                return bunny
    def choose_color(self):
        color=self.colors()[0]
        return color.get_attribute("title")

    def product_name(self):
        product_name=self.driver.find_element(By.CSS_SELECTOR,"#Description>h1")
        return product_name.text[:25]
    def price(self):
        price_element=self.driver.find_element(By.CSS_SELECTOR,"#Description>h2")
        price=''
        for i in price_element.text:
            if i.isnumeric():
                price+=i
            if i=='.':
                price+=i
        return price
