from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory" :
                                                   "/Users/ajayvidekar/Desktop"})

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver", chrome_options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='textbox']").send_keys("testing")
driver.find_element_by_id("createTxt").click()
# to download the file
driver.find_element_by_id("link-to-download").click()

driver.find_element_by_id("pdfbox").send_keys("testing")
driver.find_element_by_id("createPdf").click()
# to download the file
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(5)

driver.quit()