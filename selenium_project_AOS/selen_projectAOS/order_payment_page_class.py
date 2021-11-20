from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from sheet import AOS_Sheet


class order_payment_page:
    # define driver, wait and XL file
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.sheet = AOS_Sheet()

    # return the registration button element
    def registration(self):
        return self.driver.find_element(By.ID, "registration_btnundefined")

    # click on registration button element
    def click_registration(self):
        self.registration().click()

    # return the next button element
    def next(self):
        return self.driver.find_element(By.ID, "next_btn")

    # click on next button element
    def click_next(self):
        self.next().click()
    # return the safe pay username box element in order payment page
    def safe_pay_username(self):
        return self.driver.find_element(By.NAME, "safepay_username")

    # enter the value of safe pay username box element from the XL file
    def enter_safe_pay_username(self,test_number):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "safepay_username")))
        self.safe_pay_username().send_keys(self.sheet.get_new_safepay_username(test_number))

    # return the safe pay password box element in order payment page
    def safe_pay_password(self):
        return self.driver.find_element(By.NAME, "safepay_password")

    # enter the value of safe pay password box element from the XL file
    def enter_safe_pay_password(self,test_number):
        self.safe_pay_password().send_keys(self.sheet.get_new_safepay_password(test_number))

    # return the pay-now button element
    def pay_now(self):
        return self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")

    # click on pay-now button element
    def click_pay_now(self):
        self.pay_now().click()

    # return the element where is written order completed
    def completed_payment(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate='Thank_you_for_buying_with_Advantage']")))
        return self.driver.find_element(By.CSS_SELECTOR, "[translate='Thank_you_for_buying_with_Advantage']")

    # return login button element
    def login(self):
        return self.driver.find_element(By.ID, "login_btnundefined")

    # click on login button
    def click_login(self):
        self.login().click()

    # return the username element in order payment page
    def username(self):
        username = self.driver.find_element(By.NAME, "usernameInOrderPayment")
        return username

    # enter a value from XL file by take the number of the test
    def enter_username(self, test_number):
        username = self.username()
        username.click()
        username.clear()
        username.send_keys(self.sheet.get_exist_username(test_number))

    # return the password element in order payment page
    def password(self):
        password = self.driver.find_element(By.NAME, "passwordInOrderPayment")
        return password

    # enter a value from XL file by take the number of the test
    def enter_password(self, test_number):
        password = self.password()
        password.click()
        password.clear()
        password.send_keys(self.sheet.get_exist_password(test_number))

    # return master card radio button
    def master_card_radio(self):
        return self.driver.find_element(By.NAME, "masterCredit")

    # click on the master-card radio element
    def click_master_credit(self):
        self.master_card_radio().click()

    # return the card number box element
    def card_number(self):
        return self.driver.find_element(By.NAME, "card_number")

    # return the CVV box element
    def CVV_number(self):
        return self.driver.find_element(By.NAME, "cvv_number")

    # return the MM select element
    def date_mounth(self):
        return Select(self.driver.find_element(By.NAME, "mmListbox"))

    # return the YYYY select element
    def date_year(self):
        return Select(self.driver.find_element(By.NAME, "yyyyListbox"))

    # return the holder-name box element
    def card_holder_name(self):
        return self.driver.find_element(By.NAME, "cardholder_name")

    # get test number and fill the card number box by XL file
    def fill_card_number(self,test_number):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "card_number")))
        card_num_element = self.card_number()
        card_num_element.send_keys(Keys.DELETE)
        card_num_element.send_keys(self.sheet.get_card_number(test_number))

    # get test number and fill the CVV box by XL file
    def fill_CVV(self,test_number):
        CVV_element = self.CVV_number()
        CVV_element.clear()
        CVV_element.send_keys(self.sheet.get_CVV(test_number))
        CVV_element.clear()
        CVV_element.send_keys(self.sheet.get_CVV(test_number))

    # get test number and fill the holder name box by XL file
    def fill_holder_name(self,test_number):
        holder_element = self.card_holder_name()
        holder_element.clear()
        holder_element.send_keys(self.sheet.get_holder_name(test_number))

    # get test number and fill the month box by XL file
    def fill_MM(self,test_number):
        self.date_mounth().select_by_visible_text(self.sheet.get_MM(test_number))
    # get test number and fill the year box by XL file
    def fill_YYYY(self,test_number):
        self.date_year().select_by_visible_text(self.sheet.get_YYYY(test_number))

    # return the pay-now master card element
    def pay_now_master_card(self):
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")

    # click on pay-now master card element
    def click_pay_now_master_card(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "pay_now_btn_ManualPayment")))
        self.pay_now_master_card().click()

    # return the edit element button
    def edit_element(self):
        return self.driver.find_element(By.CLASS_NAME, "edit")

    # click on edit element button
    def click_edit(self):
        self.edit_element().click()

    # return the number of the order after make an order
    def order_number(self):
        self.wait.until(EC.visibility_of_element_located((By.ID,"orderNumberLabel")))
        return self.driver.find_element(By.ID,"orderNumberLabel")

