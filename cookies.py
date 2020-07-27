from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")

driver.get("https://www.amazon.in")

# Capture all the cookies created by browser
cookies = driver.get_cookies()

# Print number of cookies
print(len(cookies))

# Print all the cookies
print(cookies)

print("--------------------------------------------------")
# add new cookie to browser
cookie = {'name' : "my_cookie", 'value' : "1234567890"}
driver.add_cookie(cookie)

# Capture all the cookies created by browser
cookies = driver.get_cookies()
# Print number of cookies
print(len(cookies))
# Print all the cookies
print(cookies)

print("--------------------------------------------------")
# delete a cookie
driver.delete_cookie('my_cookie')

# Capture all the cookies created by browser
cookies = driver.get_cookies()
# Print number of cookies
print(len(cookies))
# Print all the cookies
print(cookies)

print("--------------------------------------------------")
# Delete all cookies
driver.delete_all_cookies()
# Capture all the cookies created by browser
cookies = driver.get_cookies()
# Print number of cookies
print(len(cookies))
# Print all the cookies
print(cookies)