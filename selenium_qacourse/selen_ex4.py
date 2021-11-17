from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from time import sleep


service = Service(r"C:\chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
driver.implicitly_wait(10)

username=driver.find_element(By.CSS_SELECTOR,'input[name="userName"]')
username.send_keys("tutorial")

pwd=driver.find_element(By.CSS_SELECTOR,'input[name="password"]')
pwd.send_keys("tutorial")

driver.find_element(By.CSS_SELECTOR,'input[name="submit"]').click()
driver.find_element(By.LINK_TEXT,"Flights").click()
driver.find_element(By.CSS_SELECTOR,"input[value='oneway']").click()

departure=driver.find_element(By.NAME,"fromPort")
departure_dropdown=Select(departure)
departure_dropdown.select_by_visible_text("Sydney")

driver.find_element(By.CSS_SELECTOR,'input[value="First"]').click()

sleep(4)
driver.find_element(By.CSS_SELECTOR,'input[name="findFlights"]').click()
