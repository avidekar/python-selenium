from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# how to find the total number of input boxes in web page
input_boxes = driver.find_elements(By.CLASS_NAME, 'text_field') #all the text boxes on html page
# has common text_field in the given URL
print(len(input_boxes))

# How to enter value into text box
print(driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed())
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Ajay")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("Videkar")
driver.find_element_by_id('RESULT_TextField-3').send_keys("111-111-1111")
