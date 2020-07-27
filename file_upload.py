from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
driver.get("http://testautomationpractice.blogspot.com/")

driver.switch_to_frame(0)

#driver.find_element_by_id("RESULT_FileUpload-11").send_keys("/Users/ajayvidekar/Desktop/test.docx")

driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']").send_keys("/Users/ajayvidekar/Desktop/test.docx")

