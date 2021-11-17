from selenium import webdriver
import selenium_booking.constants as const
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Booking:
    def __init__(self,driver_path=r"C:\chromedriver_win32\chromedriver"):
        service = Service(driver_path)
        self.driver=webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)

