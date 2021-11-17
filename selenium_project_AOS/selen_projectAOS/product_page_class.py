import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from sheet import AOS_Sheet

class product_page:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
        self.sheet = AOS_Sheet()

    def add_to_cart(self):
        add_to_cart_element=self.driver.find_element(By.NAME,"save_to_cart")
        return add_to_cart_element

    def click_add_to_cart(self):
        self.add_to_cart().click()

    def quantity(self):
        return self.driver.find_element(By.NAME,"quantity")

    def enter_quantity(self,test_number,product_number):
        self.quantity().click()
        self.quantity().send_keys(Keys.BACK_SPACE)
        quantity=self.sheet.get_Quantity(test_number,product_number)
        self.quantity().send_keys(f"{quantity}")
        return int(quantity)

    def change_quantity(self):
        self.quantity().click()
        self.quantity().send_keys(Keys.BACK_SPACE)
        quantity=random.randint(1,4)
        self.quantity().send_keys(f"{quantity}")
        return quantity


    def colors(self,test_number,product_number):
        colors_elements=self.driver.find_elements(By.CSS_SELECTOR,".productColor")
        if self.sheet.get_Category(test_number, product_number) == "laptops" or self.sheet.get_Category(test_number,product_number) == "mice":
            colors_elements_len = int(len(colors_elements) / 2 - 1)
            for x in range(colors_elements_len):
                colors_elements.remove(colors_elements[x])
        for i in colors_elements:
                    if i.get_attribute("title") == self.sheet.get_Color(test_number, product_number):
                        return i

    def choose_color(self,test_number,product_number):
        colors_elements = self.driver.find_elements(By.CSS_SELECTOR, ".productColor")
        if self.sheet.get_Category(test_number, product_number) == "laptops" or self.sheet.get_Category(test_number,product_number) == "mice":
            colors_elements_len=int(len(colors_elements)/2-1)
            for x in range(colors_elements_len):
                colors_elements.remove(colors_elements[x])
        color=self.colors(test_number, product_number)
        if colors_elements.index(color)!=0:
            color.click()
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

    def click_back_to_home(self):
        self.driver.find_element(By.CSS_SELECTOR, "[translate='HOME']").click()
