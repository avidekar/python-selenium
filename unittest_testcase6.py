import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def test_name(self):
        driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
        driver.get("https://www.google.com")
        title_of_the_page = driver.title
        #self.assertTrue(title_of_the_page == "Google") # True
        #self.assertTrue(title_of_the_page == "Google123")  # False
        #self.assertFalse(title_of_the_page == "Google") # False
        self.assertFalse(title_of_the_page == "Google123")  # False

if __name__ == "__main__":
    unittest.main()
