import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sheet import AOS_Sheet

class product_page:
    # constructor function get driver define driver wait object and AOS_sheet object
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
        self.sheet = AOS_Sheet()

    # add_to_cart returns the element of add to cart button
    def add_to_cart(self):
        return self.driver.find_element(By.NAME,"save_to_cart")

    # click_add_to_cart call to add_to_cart function and click on element
    def click_add_to_cart(self):
        self.add_to_cart().click()

    # returns element of quantity input
    def quantity(self):
        return self.driver.find_element(By.NAME,"quantity")

    # enter_quantity call to quantity function and insert new quantity
    def enter_quantity(self,test_number,product_number):
        self.quantity().click()
        self.quantity().send_keys(Keys.BACK_SPACE)
        quantity=self.sheet.get_Quantity(test_number,product_number)
        self.quantity().send_keys(f"{quantity}")
        return int(quantity)

    # enter_quantity call to quantity function and change quantity
    def change_quantity(self):
        self.quantity().click()
        self.quantity().send_keys(Keys.BACK_SPACE)
        quantity=random.randint(1,4)
        self.quantity().send_keys(f"{quantity}")
        return quantity

    # returns the color element
    def color(self,test_number,product_number):
        colors_elements=self.driver.find_elements(By.CSS_SELECTOR,".productColor")
        # check if category is leptops or mice(because in this categories the colors elements presented twice)
        if self.sheet.get_Category(test_number, product_number) == "laptops" or self.sheet.get_Category(test_number,product_number) == "mice":
            colors_elements_len = int(len(colors_elements) / 2 - 1)
            # delete half of the list
            for x in range(colors_elements_len):
                colors_elements.remove(colors_elements[x])
        # search the specific color in list
        for i in colors_elements:
                    if i.get_attribute("title") == self.sheet.get_Color(test_number, product_number):
                        return i

    # click the color element which chose and return the color
    def choose_color(self,test_number,product_number):
        colors_elements = self.driver.find_elements(By.CSS_SELECTOR, ".productColor")
        # check if category is leptops or mice(because in this categories the colors elements presented twice)
        if self.sheet.get_Category(test_number, product_number) == "laptops" or self.sheet.get_Category(test_number,product_number) == "mice":
            colors_elements_len=int(len(colors_elements)/2-1)
            # delete half of the list
            for x in range(colors_elements_len):
                colors_elements.remove(colors_elements[x])
        color=self.color(test_number, product_number)
        # check if the index of the number is not zero because this element clicked by default
        if colors_elements.index(color)!=0:
            color.click()
        return color.get_attribute("title")

    # product_name returns the product name first 25 letters
    def product_name(self):
        product_name=self.driver.find_element(By.CSS_SELECTOR,"#Description>h1")
        return product_name.text[:25]

    # price_element returns the element of the product price
    def price_element(self):
        return self.driver.find_element(By.CSS_SELECTOR,"#Description>h2")

    # price return the price of product
    def price(self):
        price=''
        # keep in string only the numeric letters
        for i in self.price_element().text:
            if i.isnumeric():
                price+=i
            if i=='.':
                price+=i
        return price

    # returns element of home page link
    def back_to_home(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='HOME']")

    # call back_to_home for element and click on it
    def click_back_to_home(self):
        self.back_to_home().click()
