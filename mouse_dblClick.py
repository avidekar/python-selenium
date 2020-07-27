from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)

# double click on button
actions.double_click(element).perform()

