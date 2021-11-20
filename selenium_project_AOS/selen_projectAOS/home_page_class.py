from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from sheet import AOS_Sheet


class home_page:
    # constructor function get driver define driver wait object and AOS_sheet object
    def __init__(self,driver:webdriver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
        self.sheet=AOS_Sheet()

    # category function get test number and product number and returns the element of the product category
    def category(self,test_number,product_number):
        self.wait.until(EC.invisibility_of_element_located((By.ID, "checkOutPopUp")))
        categories_element=self.driver.find_element(By.ID,f"{self.sheet.get_Category(test_number,product_number)}Img")
        return categories_element

    # click_category call category function to get category element and click on it
    def click_category(self,test_number,product_number):
        self.category(test_number,product_number).click()

    # user_emoji returns the element of the menu user item
    def user_emoji(self):
        return self.driver.find_element(By.ID,"menuUserLink")

    # user_emoji_click call user_emoji to get the element and click on it
    def user_emoji_click(self):
        self.wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME,"PopUp")))
        self.user_emoji().click()

    # username returns the element of the menu user input
    def username(self):
        return self.driver.find_element(By.NAME,"username")

    # enter_username get user name call username function to get the element clear it and insert the username
    def enter_username(self,username):
        self.username().clear()
        self.username().send_keys(username)

    # password returns the element of the password input
    def password(self):
        return self.driver.find_element(By.NAME,"password")

    # enter_password get password call password function to get the element clear it and insert the username
    def enter_password(self,password):
        self.password().clear()
        self.password().send_keys(password)

    # sign_in returns the element of the sign in button
    def sign_in(self):
        return self.driver.find_element(By.ID,"sign_in_btnundefined")

    # sign_in_click call sign_in to get the element and click on it
    def sign_in_click(self):
        self.wait.until_not(EC.visibility_of_element_located((By.ID,"loader")))
        self.sign_in().click()

    # sign_out returns the element of the sign out button
    def sign_out(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[ng-click='signOut($event)']")

    # sign_in_click call sign_out to get the element and click on it
    def click_sign_out(self):
        self.sign_out().click()

    # shopping_cart_window returns the element of the shopping cart window logo
    def shopping_cart_window(self):
        return self.driver.find_element(By.ID,"menuCart")

    # click_shopping_cart_window function call shopping_cart_window to get the element and click on it
    def click_shopping_cart_window(self):
        self.shopping_cart_window().click()

    # names_in_cart returns the products names in shopping cart window
    def names_in_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"table>tbody>tr[id='product']>td>a>h3")))
        names_elements=self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr[id='product']>td>a>h3")
        products_names=[]
        for products_name in names_elements:
            # the inner text of product name element after 25 letters contain dots("...")
            products_names.append(products_name.text[:25])
        return products_names

    # quantities_in_cart returns list of the quantity of each product in cart
    def quantities_in_cart(self):
        # find quantity element
        quantities_elements = self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr[id='product']>td>a>label")
        quantities=[]
        # for each element keep in list only the quantities values
        for i in range(0,len(quantities_elements),2):
            qu=quantities_elements[i].text.split()
            quantities.append(int(qu[-1]))
        return quantities

    # colors_in_cart returns list of the color of each product in cart
    def colors_in_cart(self):
        colors_elements=self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr[id='product']>td>a>label>span")
        colors=[]
        # append to list the colors
        for color in colors_elements:
            colors.append(color.text)
        return colors

    # total_price returns the total price which presented in the cart window
    def total_price(self):
        price_element=self.driver.find_elements(By.CSS_SELECTOR,"tfoot>tr>td>span")
        price=''
        # save in string only the number in the inner text of the element
        for i in price_element[1].text:
            if i.isnumeric():
                price+=i
            if i=='.':
                price+=i
        return float(price)

    # remove returns the element of the remove
    def remove(self):
        return self.driver.find_elements(By.CLASS_NAME,"iconX")

    # click_remove call remove to get elements and click to remove the first product
    def click_remove(self):
        self.remove()[0].click()

    # len_of_products_in_Cart return length of list of the products elements in cart
    def len_of_products_in_Cart(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr"))

    # return the total items in cart
    def total_items_in_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "checkOutPopUp")))
        string_of_items = self.driver.find_element(By.CSS_SELECTOR, "td>span>label").text
        number_of_items = ""
        for w in string_of_items:
            if w.isnumeric():
                number_of_items += w
        return number_of_items

    # check if page is home
    def check_if_page_is_home(self):
        if EC.invisibility_of_element_located((By.CSS_SELECTOR,"[translate='HOME']")):
            return True
        return False

    # returns checkout element
    def checkout(self):
        return self.driver.find_element(By.ID, "checkOutPopUp")

    # call checkout to get element and click on it
    def click_checkout(self):
        self.checkout().click()

    # returns my orders element
    def my_orders(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"[translate='My_Orders']")

    # call my_orders to get elements and click on the second one which take you to my orders page
    def click_my_orders(self):
        self.wait.until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate='Your_shopping_cart_is_empty']")))
        self.my_orders()[1].click()

    # check if user logged in returns true or false
    def check_if_the_user_sign(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='hi-user containMiniTitle ng-binding']")))
        text = self.driver.find_elements(By.CSS_SELECTOR, "[class='hi-user containMiniTitle ng-binding']")
        if len(text) == 1:
            return True
        return False

    # check if user logged out returns true or false
    def check_if_the_user_NOT_sign(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "[class='hi-user containMiniTitle ng-binding']")))
        text = self.driver.find_elements(By.CSS_SELECTOR, "[class='hi-user containMiniTitle ng-binding']")
        if len(text) == 0:
            return True
        return False

    # get test number and returns the username which returned from self.sheet.get_exist_username()
    def get_exist_username(self, test_number):
        return self.sheet.get_exist_username(test_number)

    # get test number and returns the username which returned from self.sheet.get_exist_username()
    def get_exist_password(self, test_number):
        return self.sheet.get_exist_password(test_number)






