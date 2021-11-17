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

    def tracking_numbers(self):
        elements=self.driver.find_elements(By.CSS_SELECTOR, "[data-ng-repeat-start='order in myOrdersCtrl.orders track by $index'']>td>label")
        tracking_numbers=[]
        for i in elements:
            if i.text.isalnum():
                tracking_numbers.append(i.text)
        return tracking_numbers
