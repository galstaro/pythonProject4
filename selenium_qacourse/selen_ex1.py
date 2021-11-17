from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

service = Service(r"C:\chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://phptravels.net/api/admin")
driver.maximize_window()

# In case an element is not found - define 10 sec timeout
driver.implicitly_wait(10)

email_line=driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(1) > form.form-signin.form-horizontal.wow.fadeIn.animated.animated > div:nth-child(1) > label:nth-child(2) > input[type=text]")

email_line.send_keys("admin@phptravels.com")

password_line=driver.find_element(By.CSS_SELECTOR,'input[placeholder="Password"]')

password_line.send_keys("demoadmin")

login_button=driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')

login_button.click()

if driver.find_element(By.CSS_SELECTOR,"a[class=navbar-brand]>strong>small").text=="DASHBOARD":
    print("test passed")
else:
    print("test failed")

logout=driver.find_element(By.CSS_SELECTOR,'i[class="fa fa-sign-out"]')
logout.click()
driver.close()