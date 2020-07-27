from selenium import webdriver
driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get("http://newtours.demoaut.com/mercurywelcome.php")
driver.maximize_window()

#driver.save_screenshot("/Users/ajayvidekar/Desktop/homepage.png")

driver.get_screenshot_as_file("/Users/ajayvidekar/Desktop/homepage.png") # only supports png and
# warns against other file types