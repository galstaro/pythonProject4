from selenium import webdriver
from selenium.webdriver.common.by import By
import random

class Category_Page:
    def __init__(self,driver):
        self.driver=driver

    def category(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"div[id='SidebarContent']>a")

    def choose_category_randomly(self):
        random.choice(self.category()).click()


class Products_Page:
    def __init__(self,driver):
        self.driver=driver

    def product_id(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "td>a")

    def choose_product_randomly(self):
        random.choice(self.product_id()).click()


class Items_Page:
    def __init__(self, driver):
        self.driver = driver

    def item_id(self):
        return self.driver.find_elements(By.PARTIAL_LINK_TEXT,"EST")

    def choose_item_randomly(self):
        random.choice(self.item_id()).click()


class Item_Page:
    def __init__(self,driver):
        self.driver=driver

    def add_to_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR,"td>a")

    def click_add_to_cart(self):
        self.add_to_cart().click()


class Shopping_Cart_Page:
    def __init__(self,driver):
        self.driver=driver

    def item_line(self):
        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        tdies = tr[len(tr) - 2].find_elements(By.CSS_SELECTOR, "td")
        return tdies

    def quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, f"input[name='{self.item_line()[0].text}']")

    def enter_random_quantity(self):
        q=self.quantity()
        q.clear()
        number= random.randint(1, 5)
        q.send_keys(number)
        return number

    def update_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR,"input[value='Update Cart']")

    def click_update_cart(self):
        self.update_cart().click()

    def list_price(self):
        x=self.item_line()[5].text[1:]
        if x.count(",")>0:
            x=x[:x.index(",")]+x[x.index(",")+1:]
        return float(x)

    def total_price(self):
        x=self.item_line()[6].text[1:]
        if x.count(",")>0:
            x=x[:x.index(",")]+x[x.index(",")+1:]
        return float(x)

    def back_link(self):
        return self.driver.find_element(By.CSS_SELECTOR,'div[id="BackLink"]>a')

    def click_back_link(self):
        self.back_link().click()

    def subtotal_price(self):
        tr = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        sub=tr[len(tr) - 1].find_elements(By.CSS_SELECTOR, "td")
        sub=sub[0].text[sub[0].text.index("$")+1:]
        if sub.count(",")>0:
            sub=sub[:sub.index(",")]+sub[sub.index(",")+1:]
        return float(sub)



