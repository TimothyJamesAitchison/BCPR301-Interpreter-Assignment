import unittest
from validator import Validator


class ValidatorTests(unittest.TestCase):
    global v
    v = Validator()

    def test_id(self):
        self.assertTrue(v.check_id('UY7'))

    def test_gender(self):
        self.assertTrue(v.check_gender('M'))
#hasitha
    def test_age(self):
        self.assertTrue(v.check_age(22))

    def test_sales(self):
        self.assertTrue(v.check_sales('66'))

    def test_bmi(self):
        self.assertTrue(v.check_bmi('NORMAL'))

    def test_salary(self):
        self.assertTrue(v.check_salary('88,412'))

    def test_birthday(self):
        self.assertTrue(v.check_birthday('22-3-1999'))



if __name__  ==" __main__":
    unittest.main()
