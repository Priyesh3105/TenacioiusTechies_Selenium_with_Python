import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

# get all the test methods from each and every file
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# CREATE TEST SUITES
sanityTestSuite=unittest.TestSuite([tc1, tc2])
functionalTestSuite=unittest.TestSuite([tc3, tc4])
masterTestSuite=unittest.TestSuite([tc1, tc2, tc3, tc4])

unittest.TextTestRunner().run(sanityTestSuite)
#unittest.TextTestRunner().run(functionalTestSuite)
#unittest.TextTestRunner(verbosity=2).run(masterTestSuite)