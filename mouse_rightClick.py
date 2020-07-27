from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions = ActionChains(driver)

# right click on button
actions.context_click(button).perform()
