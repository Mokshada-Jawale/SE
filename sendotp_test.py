import sendotp
import unittest

class TestSendOtp(unittest.TestCase):
    def test_is_email(self):
        testcase1 = 'abc26@gmail.com'
        expected1 = True
        testcase2 = 'abc.xyz90@gmail.com'
        expected2 = True
        testcase3 = 'abc-pqr@gmail.com'
        expected3 = False
        testcase4 = 'abc.gmail.com'
        expected4 = False
        self.assertEqual(sendotp.is_email(testcase1), expected1)
        self.assertEqual(sendotp.is_email(testcase2), expected2)
        self.assertEqual(sendotp.is_email(testcase3), expected3)
        self.assertEqual(sendotp.is_email(testcase4), expected4)

    def test_generate_otp(self):
        generated = len(sendotp.generate_otp())
        expected = 6
        self.assertEqual(generated,expected)

    def test_verify_otp(self):
        testcase = 345678
        expected = 345678
        self.assertTrue(sendotp.verify_otp(testcase,expected))

    # def test_verify(self):
    #     expected = sendotp.verify_otp(sendotp.generate_otp(),sendotp.OTP)
    #     self.assertEqual(True,expected)

if __name__ == '__main__':
    unittest.main()