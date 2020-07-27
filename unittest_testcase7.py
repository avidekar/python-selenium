import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_name(self):
        driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
        self.assertIsNotNone(driver) # True
        #driver = None
        #self.assertIsNone(driver) # False

if __name__ == "__main__":
    unittest.main()