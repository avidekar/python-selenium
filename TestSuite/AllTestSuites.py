import unittest
from package1.TC_LoginTest import LoginTest
from package1.TC_SignUpTest import SignUpTest

from package2.TC_PaymentTest import PaymentTest
from package2.TC_PaymentReturnsTest import PaymentReturnsTest

# Get all tests from all the class imported - LoginTest, SignUpTest, PaymentTest, PaymentReturnsTest
tc_login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc_signup = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc_payment = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc_payment_returns = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating Test Suites

# Sanity Test Suite
# sanity_test_suite = unittest.TestSuite([tc_login, tc_signup])
# unittest.TextTestRunner().run(sanity_test_suite)

# Functional Test Suite
# functional_test_suite = unittest.TestSuite([tc_payment, tc_payment_returns])
# unittest.TextTestRunner().run(functional_test_suite)

# Master Test Suite
master_test_suite = unittest.TestSuite([tc_signup, tc_login, tc_payment, tc_payment_returns])
unittest.TextTestRunner(verbosity=2).run(master_test_suite)




