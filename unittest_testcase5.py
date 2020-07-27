import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_name(self):
        driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
        driver.get("https://www.google.com")
        title = driver.title
        #self.assertEqual("Google", title, "Webpage title does not match") #PASS
        #self.assertEqual("Google1233", title, "Webpage title does not match") #FAIL
        #self.assertNotEqual("Google1233", title, "Webpage title does not match") #PASS
        self.assertNotEqual("Google", title, "Webpage title does not match") #FAIL

if __name__ == "__main__":
    unittest.main()