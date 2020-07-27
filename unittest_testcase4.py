import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest # called as decorator to skip tests
    def test_search(self):
        print("This is search test")

    @unittest.skip("Skipping this test because it is not ready")
    def test_advanced_search(self):
        print("This is advanced search test")

    @unittest.skipIf(1==1,"One is equal to One")
    def test_prepaid_charge(self):
        print("This is prepaid charge test")

    def test_postpaid_charge(self):
        print("This is postpaid charge test")

    def test_loginbygmail(self):
        print("This is login by email test")

    def test_loginbytwitter(self):
        print("This is login by twitter test")

if __name__ == "__main__":
    unittest.main()