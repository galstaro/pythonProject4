from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from sheet import AOS_Sheet


class create_account_page:

    # constructor function get driver define driver wait object and AOS_sheet object
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
        self.sheet=AOS_Sheet()

    # username returns element of username field
    def username(self):
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    # password returns element of password field
    def password(self):
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    # email returns element of email field
    def email(self):
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    # confirm_password returns element of confirm password field
    def confirm_password(self):
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    # enter_username call username and insert username from sheet
    def enter_username(self,test_number):
        self.username().send_keys(self.sheet.get_new_username(test_number))

    # enter_password call password and insert password from sheet
    def enter_password(self,test_number):
        self.password().send_keys(self.sheet.get_new_password(test_number))

    # enter_email call email and insert email from sheet
    def enter_email(self,test_number):
        self.email().send_keys(self.sheet.get_new_mail(test_number))

    # enter_confirm_password call confirm_password and insert password from sheet
    def enter_confirm_password(self,test_number):
        self.confirm_password().send_keys(self.sheet.get_new_password_to_confirm(test_number))

    # conditions_of_use_agreement returns element of conditions_of_use_agreement
    def conditions_of_use_agreement(self):
        return self.driver.find_element(By.NAME, "i_agree")

    # click_conditions_of_use_agreement call conditions_of_use_agreement and click in it
    def click_conditions_of_use_agreement(self):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "i_agree")))
        self.conditions_of_use_agreement().click()

    # register returns element of register
    def register(self):
        return self.driver.find_element(By.ID,"register_btnundefined")

    # click_register call register and click in it
    def click_register(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "register_btnundefined")))
        self.register().click()
        self.register().send_keys(Keys.ENTER)
