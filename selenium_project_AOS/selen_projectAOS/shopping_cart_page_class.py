from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
from time import sleep

class shopping_cart_page:
    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)

    def title(self):
        title=self.driver.find_element(By.CLASS_NAME,"select")
        return title

    def title_text_shopping_cart(self):
        return self.title().text

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
        self.wait.until_not(EC.element_to_be_clickable((By.ID, "checkOutPopUp")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "EDIT")))
        return self.driver.find_elements(By.LINK_TEXT,"EDIT")

    def checkout(self):
        return self.driver.find_element(By.ID,"checkOutButton")

    def click_checkout(self):
        self.checkout().click()

    def shopping_cart_empty(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate='Your_shopping_cart_is_empty']")))
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='Your_shopping_cart_is_empty']")

    def quantities_in_cart(self):
        quantities=self.driver.find_elements(By.CSS_SELECTOR,".quantityMobile>label[class='ng-binding']")
        after_change_quantities=[]
        for i in quantities:
            after_change_quantities.append(int(i.text))
        return after_change_quantities