import unittest
from selenium import webdriver

class SearchEngines(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
        self.driver.get("https://www.google.com")
        print(self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="/Users/ajayvidekar/Downloads/chromedriver")
        self.driver.get("https://www.bing.com")
        print(self.driver.title)
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
