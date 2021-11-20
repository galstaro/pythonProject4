from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class shopping_cart_page:

    # define driver, wait and XL file
    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)

    # return the element of the title in shopping cart
    def title(self):
        title=self.driver.find_element(By.CLASS_NAME,"select")
        return title

    # return the text of the title element in shopping cart
    def title_text_shopping_cart(self):
        return self.title().text

    # return the text of the price in shopping cart
    def text_price(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"cart-total")))
        total_price_elements=self.driver.find_elements(By.CLASS_NAME,"cart-total")
        return total_price_elements[0].text

    # return the numeric text of the price in shopping cart
    def price(self):
        price=''
        for w in self.text_price():
            if w.isnumeric() or w=='.':
                price+=w
        return price

    # return the list of all the edit button in shopping cart
    def edit(self):
        self.wait.until_not(EC.element_to_be_clickable((By.ID, "checkOutPopUp")))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "EDIT")))
        return self.driver.find_elements(By.LINK_TEXT,"EDIT")

    # return the checkout button
    def checkout(self):
        return self.driver.find_element(By.ID,"checkOutButton")

    # click on checkout button
    def click_checkout(self):
        self.checkout().click()

    # return the element of the title of the shopping cart condition
    def shopping_cart_empty(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate='Your_shopping_cart_is_empty']")))
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='Your_shopping_cart_is_empty']")

    # return a list of quantities in shopping cart
    def quantities_in_cart(self):
        quantities=self.driver.find_elements(By.CSS_SELECTOR,".quantityMobile>label[class='ng-binding']")
        after_change_quantities=[]
        for i in quantities:
            after_change_quantities.append(int(i.text))
        return after_change_quantities