from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

# will give url of current window
print(driver.current_window_handle) #CDwindow-9B23480BEC7FAC2EDDB8FB4F0C2F429C

# will get list of all handle values of open browsers
handles = driver.window_handles

for handle in handles:
    # switch to that handle
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()

# driver.quit()

