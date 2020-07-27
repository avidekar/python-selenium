from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
driver.get("http://newtours.demoaut.com")

user_ele = driver.find_element_by_name("userName")

print(user_ele.is_displayed()) # will return True or False on element state
print(user_ele.is_enabled()) # will return True or False on element state

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed()) # will return True or False on element state
print(pwd_ele.is_enabled()) # will return True or False on element state

user_ele.send_keys("mercury") # typing into username text box
pwd_ele.send_keys("mercury")  # typing into pssword text box

driver.find_element_by_name("login").click()

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of the roundtrip radio button : ",roundtrip_radio.is_selected()) # will return True or False

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("status of the roundtrip radio button : ", onetrip_radio.is_selected()) # will return True or False

