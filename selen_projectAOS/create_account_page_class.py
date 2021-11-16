from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep

class create_account_page:
    def __init__(self,driver):
        self.driver=driver

    def username(self):
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def password(self):
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def email(self):
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def confirm_password(self):
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def enter_username(self):
        self.username().send_keys("sdhgd12316")

    def enter_password(self):
        self.password().send_keys("As098")

    def enter_email(self):
        self.email().send_keys("sdhF1166@gmail.com")

    def enter_confirm_password(self):
        self.confirm_password().send_keys("As098")

    def conditions_of_use_agreement(self):
        return self.driver.find_element(By.NAME, "i_agree")

    def click_conditions_of_use_agreement(self):
        self.conditions_of_use_agreement().click()

    def register(self):
        return self.driver.find_element(By.ID,"register_btnundefined")

    def click_register(self):
        self.register().click()
        self.register().send_keys(Keys.ENTER)
