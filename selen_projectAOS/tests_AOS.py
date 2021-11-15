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
from category_page_class import category_page
from product_page_class import product_page
from unittest import TestCase


class tests_AOS(TestCase):
    def setUp(self):
        print("setUp")
        service1 = Service(r"C:\chromedriver_win32/chromedriver")
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get("https://advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.home=home_page(self.driver)
        self.category=category_page(self.driver)
        self.product=product_page(self.driver)

    def tearDown(self):
        sleep(10)
        self.driver.close()
        print("tearDown")

    def test1(self):
        total_items=0
        for i in range(3):
            self.home.click_category()
            self.category.click_product()
            quantity=self.product.change_quantity()
            total_items+=quantity
            self.product.click_add_to_cart()
            self.driver.find_element(By.CSS_SELECTOR,"[translate='HOME']").click()
        string_of_items=self.driver.find_element(By.CSS_SELECTOR,"td>span>label").text
        number_of_items=""
        for w in string_of_items:
            if w.isnumeric():
                number_of_items+=w
        self.assertEqual(total_items,int(number_of_items))

    def test2(self):
        qu=[]
        co=[]
        names=[]
        price=[]
        for i in range(3):
            self.home.click_category()
            self.category.click_product()
            quantity=self.product.change_quantity()
            qu.append(quantity)
            color=self.product.choose_color()
            co.append(color)
            product_name=self.product.product_name()
            names.append(product_name)
            pr=self.product.price()
            price.append(float(pr))
            self.product.click_add_to_cart()
            self.driver.find_element(By.CSS_SELECTOR,"[translate='HOME']").click()
        names.reverse()
        self.assertListEqual(names,self.home.names_in_cart())
        qu.reverse()
        self.assertListEqual(qu,self.home.quantities_in_cart())
        co.reverse()
        price.reverse()
        print(co)
        print(self.home.colors_in_cart())
        exept_price = 0.0
        for i in range(3):
            exept_price += qu[i] * price[i]
        # self.assertListEqual(self.home.colors_in_cart(),co)
        self.assertEqual(round(exept_price,2),self.home.price())

    def test3(self):
        total_items = 0
        for i in range(3):
            self.home.click_category()
            self.category.click_product()
            self.product.click_add_to_cart()
            self.driver.find_element(By.CSS_SELECTOR, "[translate='HOME']").click()

        number_of_products=self.home.len_of_products_in_Cart()
        self.home.click_remove()
        number_products_after_remove=self.home.len_of_products_in_Cart()
        self.assertEqual(number_of_products,number_products_after_remove+1)








