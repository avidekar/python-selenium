import unittest

class PaymentTest(unittest.TestCase):

    def test_payment_in_dollar_test(self):
        print("This is payment in dollar test")
        self.assertTrue(True)

    def test_payment_in_rupees_test(self):
        print("This is payment in rupees test")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
