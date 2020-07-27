from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get("http://newtours.demoaut.com")

links = driver.find_elements(By.TAG_NAME, "a")

# print the number of links present in a page
print(len(links))

# print all the links
for link in links:
    print(link.text)

# clicking on the link
#driver.find_element(By.LINK_TEXT, "REGISTER").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click() # can be REG or GIS or TER, case sensitive
