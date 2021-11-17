from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

service = Service(r"C:\chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.rail.co.il/")
driver.maximize_window()
# In case an element is not found - define 10 sec timeout
driver.implicitly_wait(10)

first_station=driver.find_element(By.CSS_SELECTOR,"#trainSearchMain > div > div > div > div.col-md-2.col-sm-5.col-xs-10.fromBox > div.typeahead.ng-isolate-scope > input")

first_station.send_keys("בנימינה")
if first_station.get_attribute("value")=="בנימינה":
    print("test passed")
else:
    print("test failed")
first_station.send_keys(Keys.ENTER)

second_station=driver.find_element(By.CSS_SELECTOR,"#trainSearchMain > div > div > div > div.col-md-2.col-sm-5.col-xs-10.toBox > div.typeahead.ng-isolate-scope > input")

second_station.send_keys("תל אביב - השלום")
second_station.send_keys(Keys.ENTER)

search_button=driver.find_element(By.CSS_SELECTOR,"#trainSearchMain > div > div > div > div.col-md-2.col-sm-11.col-xs-10.searchBtnBox > button")

search_button.click()

