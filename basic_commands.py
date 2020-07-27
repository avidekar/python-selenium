from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click() # will open another window

time.sleep(5)

#driver.close() # will close the first tab. the new tab opened from .click() exists
# .close() will close one browser at a time.

driver.quit() # will close all tabs