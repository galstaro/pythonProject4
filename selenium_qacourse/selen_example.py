from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

service = Service(r"C:\chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")

# In case an element is not found - define 10 sec timeout
driver.implicitly_wait(10)

# Write a text in google search line
google_search_line=driver.find_element(By.CSS_SELECTOR,".gLFyf")

google_search_line.send_keys("python")

# click on the Enter key
google_search_line.send_keys((Keys.ENTER))

# find the search button in google
#google_search_button=driver.find_element(By.CSS_SELECTOR,"body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b")

# click on the search button
#google_search_button.click()

sleep(2)

driver.close()