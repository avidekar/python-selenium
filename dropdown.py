from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id('RESULT_RadioButton-9')
drp = Select(element)

# select by visible text
#drp.select_by_visible_text('Morning')

# select by index number
#drp.select_by_index(2) # will select Afternoon

# select by value
drp.select_by_value('Radio-2') # will select Evening

# Count number of options -
# print(drp.options) # object values printed, e.g -
# <selenium.webdriver.remote.webelement.WebElement (session="b2b7badaeea58f21b54c0ba22e49c682"
print(len(drp.options))

# Capture all the options and print
all_options = drp.options
for option in all_options:
    print(option.text)