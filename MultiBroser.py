from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
driver = webdriver.Firefox(executable_path="/Users/ajayvidekar/Downloads/geckodriver")
driver.get("https://www.google.com/")
print(driver.title) # get title of the page
print(driver.current_url) # returns the current url
# print(driver.page_source) # returns html code for page
driver.close() # close browser
