from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,1000)","")

# scroll down till the element is visible
# flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[""1]/img")
# driver.execute_script("arguments[0].scrollIntoView();", flag)

# scroll till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")