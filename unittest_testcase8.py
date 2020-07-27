import unittest

class Test(unittest.TestCase):
    def test_name(self):
        # PASS
        # list = ['python', 'selenium', 'java']
        # self.assertIn("python", list)
        # FAIL
        # list = ['python', 'selenium', 'java']
        # self.assertIn("ruby", list)
        # PASS
        # list = ['python', 'selenium', 'java']
        # self.assertNotIn("ruby", list)
        # FAIL
        list = ['python', 'selenium', 'java']
        self.assertNotIn("python", list)

if __name__ == "__main__":
    unittest.main()
