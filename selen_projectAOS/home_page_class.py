from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep

class home_page:
    def __init__(self,driver:webdriver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def category(self):
        categories_elements=self.driver.find_elements(By.CSS_SELECTOR,".rowSection>div")
        categories_elements.remove(categories_elements[2])
        return categories_elements

    def click_category(self):
        random.choice(self.category()).click()

    def user_emoji(self):
        return self.driver.find_element(By.ID,"menuUserLink")

    def user_emoji_click(self):
        self.wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME,"PopUp")))
        self.user_emoji().click()

    def username(self):
        return self.driver.find_element(By.NAME,"username")

    def enter_username(self):
        self.username().clear()
        self.username().send_keys('elad1234')

    def password(self):
        return self.driver.find_element(By.NAME,"password")

    def enter_password(self):
        self.password().clear()
        self.password().send_keys('Thbyrby145')

    def sign_in(self):
        return self.driver.find_element(By.ID,"sign_in_btnundefined")

    def sign_in_click(self):
        self.wait.until_not(EC.visibility_of_element_located((By.ID,"loader")))
        self.sign_in().click()

    def sign_out(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[ng-click='signOut($event)']")

    def click_sign_out(self):
        self.sign_out().click()

    def shopping_cart_window(self):
        return self.driver.find_element(By.ID,"menuCart")

    def click_shopping_cart_window(self):
        self.shopping_cart_window().click()
    def names_in_cart(self):
        names_elements=self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr[id='product']>td>a>h3")
        products_names=[]
        for products_name in names_elements:
            products_names.append(products_name.text[:25])
        return products_names

    def quantities_in_cart(self):
        quantities_elements = self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr[id='product']>td>a>label")
        qua = []
        for i in range(0,len(quantities_elements),2):
            q=quantities_elements[i].text.split()
            qua.append(int(q[-1]))

        return qua
    def colors_in_cart(self):
        colors_elements=self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr[id='product']>td>a>label>span")
        colors=[]
        for color in colors_elements:
            colors.append(color.text)
        return colors
    def price(self):
        price_element=self.driver.find_elements(By.CSS_SELECTOR,"tfoot>tr>td>span")
        price=''
        for i in price_element[1].text:
            if i.isnumeric():
                price+=i
            if i=='.':
                price+=i
        return float(price)


    def remove(self):
        return self.driver.find_elements(By.CLASS_NAME,"iconX")

    def click_remove(self):
        self.remove()[0].click()


    def len_of_products_in_Cart(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr"))



