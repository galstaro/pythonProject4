from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep

class shopping_cart_page:
    def __init__(self,driver):
        self.driver=driver

    def title(self):
        title=self.driver.find_element(By.CSS_SELECTOR,"[class='roboto-regular center sticky fixedImportant ng-binding']")
        return title

    def title_text_shopping_cart(self):
        text=self.title().text
        return text[:13]

    def text_price(self):
        total_price_elements=self.driver.find_elements(By.CLASS_NAME,"cart-total")
        return total_price_elements[0].text

    def price(self):
        price=''
        for w in self.text_price():
            if w.isnumeric() or w=='.':
                price+=w
        return price

    def edit(self):
        return self.driver.find_elements(By.LINK_TEXT,"EDIT")

    def checkout(self):
        return self.driver.find_element(By.ID,"checkOutButton")

    def click_checkout(self):
        self.checkout().click()

    def shopping_cart_empty(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='Your_shopping_cart_is_empty']")