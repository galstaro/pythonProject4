from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep
from sheet import AOS_Sheet

class create_account_page:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
        self.sheet=AOS_Sheet()

    def username(self):
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def password(self):
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def email(self):
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def confirm_password(self):
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def enter_username(self,test_number):
        self.username().send_keys(self.sheet.get_new_username(test_number))

    def enter_password(self,test_number):
        self.password().send_keys(self.sheet.get_new_password(test_number))

    def enter_email(self,test_number):
        self.email().send_keys(self.sheet.get_new_mail(test_number))

    def enter_confirm_password(self,test_number):
        self.confirm_password().send_keys(self.sheet.get_new_password(test_number))

    def conditions_of_use_agreement(self):
        return self.driver.find_element(By.NAME, "i_agree")

    def click_conditions_of_use_agreement(self):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "i_agree")))
        self.conditions_of_use_agreement().click()

    def register(self):
        return self.driver.find_element(By.ID,"register_btnundefined")

    def click_register(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "register_btnundefined")))
        self.register().click()
        self.register().send_keys(Keys.ENTER)
