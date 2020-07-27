import XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get("http://newtours.demoaut.com")

driver.maximize_window()

path="/Users/ajayvidekar/Desktop/test_data.xlsx"

rows = XLUtils.getRowCount(path,"Sheet1")

for r in range(2, rows + 1): # avoiding first row since it is header
    result = ""
    user_name = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)
    driver.find_element_by_name("userName").send_keys(user_name)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("login").click()

    if driver.title == "Find a Flight: Mercury Tours:":
        result = "PASS"
    else:
        result = "FAIL"

    XLUtils.writeData(path,"Sheet1", r, 3, result)
    driver.find_element_by_link_text("Home").click()