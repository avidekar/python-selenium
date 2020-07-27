from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
driver.get("http://newtours.demoaut.com") # opening URL will take some time.

# wait some time here
driver.implicitly_wait(10) # time in seconds; implicit_wait always based on time

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()