import unittest
from selenium import webdriver

def setUpModule():
    # will be executed before any class or method is executed
    print("setUpModule")

def tearDownModule():
    # will be executed after completing all python module in the class
    print("tearDownModule")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self): # executes for every test case written. Execcuted before test case
        print("This is login test")

    @classmethod
    def tearDown(self): # executes for every test case written. Execcuted after test case
        print("This is logout test")

    @classmethod
    def setUpClass(cls): # only executes once
        print("Open Application")

    @classmethod
    def tearDownClass(cls): # only executes once
        print("Close Application")

    def test_search(self):
        print("This is search test")

    def test_advanced_search(self):
        print("This is advanced search test")

    def test_prepaid_charge(self):
        print("This is prepaid charge test")

    def test_postpaid_recharge(self):
        print("This is postpaid charge test")

if __name__ == "__main__":
    unittest.main()