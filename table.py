from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get("<insert_url_with_table>.html")

# will count the number of rows
num_of_rows = len(driver.find_element_by_xpath("/html/body/table/tbody/tr"))

# will count the number of columns
num_of_cols = len(driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th"))

print(num_of_rows) #5 (includes table header row as well)
print(num_of_cols) #3

print("Product      Article      Price")
for r in range(2,num_of_rows+1):
    for c in range(1, num_of_cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/th["+str(
            c)+"]").text
        #print(value, end='     ')
        print(value)
