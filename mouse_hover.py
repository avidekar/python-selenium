from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get('https://opensource-demo.orangehrmlive.com')

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")

driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")

driver.find_element_by_xpath("//*[@id='btnLogin']").click()

admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b/font/font")
usrmngt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']/font/font")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']/font/font")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usrmngt).move_to_element(users).click().perform()




