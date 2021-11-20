from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from sheet import AOS_Sheet


class category_page:

    # define driver, wait and XL file
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
        self.sheet = AOS_Sheet()

    # return the element of the product by XL file
    def products(self,test_number,product_number):
        products_element=self.driver.find_element(By.ID,f"{self.sheet.get_Product_ID(test_number,product_number)}")
        return products_element

    # click on specific product from the XL file
    def click_product(self,test_number,product_number):
        self.products(test_number,product_number).click()

    # return the title in the category page
    def category_title(self):
        text = self.driver.find_element(By.CLASS_NAME, "categoryTitle")
        return text.text
