from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
from time import sleep

class my_orders_page:
    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)

    def order_numbers(self):
        elements=self.driver.find_elements(By.CSS_SELECTOR, "tr[data-ng-repeat-start='order in myOrdersCtrl.orders track by $index']>td>label")
        order_numbers=[]
        for i in elements:
            if i.text.isalnum() and len(i.text)>1:
                order_numbers.append(i.text)
        order_numbers=set(order_numbers)
        order_numbers=list(order_numbers)
        return order_numbers
