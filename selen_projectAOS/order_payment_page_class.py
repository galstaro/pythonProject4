from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import random
from time import sleep


class order_payment_page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def registration(self):
        return self.driver.find_element(By.ID, "registration_btnundefined")

    def click_registration(self):
        self.registration().click()

    def next(self):
        return self.driver.find_element(By.ID, "next_btn")

    def click_next(self):
        self.next().click()

    def safe_pay_username(self):
        return self.driver.find_element(By.NAME, "safepay_username")

    def enter_safe_pay_username(self):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "safepay_username")))
        self.safe_pay_username().send_keys("Asdfg")

    def safe_pay_password(self):
        return self.driver.find_element(By.NAME, "safepay_password")

    def enter_safe_pay_password(self):
        self.safe_pay_password().send_keys("0987ASDg")

    def pay_now(self):
        return self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")

    def click_pay_now(self):
        self.pay_now().click()

    def completed_payment(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate='Thank_you_for_buying_with_Advantage']")))
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='Thank_you_for_buying_with_Advantage']")

    def click_login(self):
        login = self.driver.find_element(By.ID, "login_btnundefined")
        login.click()

    def username(self):
        username = self.driver.find_element(By.NAME, "usernameInOrderPayment")
        return username

    def enter_username(self, name):
        username = self.username()
        username.click()
        username.clear()
        username.send_keys(name)

    def password(self):
        password = self.driver.find_element(By.NAME, "passwordInOrderPayment")
        return password

    def enter_password(self, passw):
        password = self.password()
        password.click()
        password.clear()
        password.send_keys(passw)

    def click_next(self):
        next = self.driver.find_element(By.ID, "next_btn")
        next.click()

    def click_master_credit(self):
        master_credit = self.driver.find_element(By.NAME, "masterCredit")
        master_credit.click()

    def card_number(self):
        return self.driver.find_element(By.NAME, "card_number")

    def CVV_number(self):
        return self.driver.find_element(By.NAME, "cvv_number")

    def date_mounth(self):
        return Select(self.driver.find_element(By.NAME, "mmListbox"))

    def date_year(self):
        return Select(self.driver.find_element(By.NAME, "yyyyListbox"))

    def card_holder_name(self):
        return self.driver.find_element(By.NAME, "cardholder_name")

    def fill_master_card_details(self, card_number, cvv_number, holder_name, mm, yyyy):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "card_number")))
        card_num_element = self.card_number()
        card_num_element.send_keys(Keys.DELETE)
        card_num_element.send_keys(card_number)
        CVV_element = self.CVV_number()
        CVV_element.clear()
        CVV_element.send_keys(cvv_number)
        CVV_element.clear()
        CVV_element.send_keys(cvv_number)
        holder_element = self.card_holder_name()
        holder_element.clear()
        holder_element.send_keys(holder_name)
        self.date_mounth().select_by_index(mm)
        self.date_year().select_by_index(yyyy)

    def click_pay_now_master_card(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "pay_now_btn_ManualPayment")))
        pay_now = self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")
        pay_now.click()

    def click_edit(self):
        edit = self.driver.find_element(By.CLASS_NAME, "edit")
        edit.click()

    def order_number(self):
        self.wait.until(EC.visibility_of_element_located((By.ID,"orderNumberLabel")))
        return self.driver.find_element(By.ID,"orderNumberLabel")


