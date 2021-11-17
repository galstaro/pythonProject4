from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


service = Service(r"C:\chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://juliemr.github.io/protractor-demo/")
driver.maximize_window()
driver.implicitly_wait(10)

num1=driver.find_element(By.CSS_SELECTOR,'input[ng-model="first"]')
num1.send_keys(10)

num2=driver.find_element(By.CSS_SELECTOR,'input[ng-model="second"]')
num2.send_keys(7)
driver.find_element(By.CSS_SELECTOR,"button").click()
timeout = 5
try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'td[class=ng-binding]'))
    WebDriverWait(driver, timeout).until(element_present)
except:
    print("Timed out waiting for page to load")

result=driver.find_element(By.CSS_SELECTOR,"h2[class=ng-binding]")
if result.text=="17":
    print("test passed")
else:
    print("test failed")

driver.close()