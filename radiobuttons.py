from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Working with the radio buttons
# status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected() # returns True or False
# print(status)
# driver.find_element_by_id("RESULT_RadioButton-7_0").click()
# status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected() # returns True or False
# print(status)

# Working with check boxes
driver.find_element_by_id("RESULT_CheckBox-8_0").click()
# driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected() # to get the status
driver.find_element_by_id("RESULT_CheckBox-8_6").click()
# driver.find_element_by_id("RESULT_CheckBox-8_6").is_selected() # to get the status
