import unittest

class Test(unittest.TestCase):
    def test_name(self):
        # assertGreater - first value is greater than second value
        self.assertGreater(100, 10)
        # assertGreaterEqual - first value is greater than or Equal to second value
        self.assertGreaterEqual(100, 10)
        # assertLess - first value less than second value
        self.assertLess(10, 100)
        # assertLessEqual - first value less than  or equal to second value
        self.assertLessEqual(10, 100)

if __name__ == "__main__":
        unittest.main()
