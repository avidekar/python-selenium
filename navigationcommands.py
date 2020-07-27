from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
driver.get("http://newtours.demoaut.com")
time.sleep(3)
print(driver.title)
driver.get("http://pavantestingtools.blogspot.in")
time.sleep(3)
print(driver.title)
driver.back() # to go to previous url
time.sleep(3)
print(driver.title)
driver.forward() # to go next url
time.sleep(3)
print(driver.title)