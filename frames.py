from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()

time.sleep(3)
# to go back to default frame before going to next frame
driver.switch_to_default_content()

# switching to second frame
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()

driver.switch_to_default_content()

time.sleep(3)

# switching to third frame
driver.switch_to.frame("classFrame")

driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()
