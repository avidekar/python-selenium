from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com")

# driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID, "tab-flight-tab-hp").click()
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("04/18/2020")

driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("04/22/2020")

driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

# Explicit Waits
wait = WebDriverWait(driver, 10) # 10 here denotes maximum time out
driver.find_element(By.XPATH, "//*[@id='change-flight']/div/div[2]/div/label").click()
element = wait.until(ec.element_to_be_clickable(By.XPATH, "//*[@id='change-flight']/div/div[2]/div/label"))
element.click()

time.sleep(3)
driver.quit()
