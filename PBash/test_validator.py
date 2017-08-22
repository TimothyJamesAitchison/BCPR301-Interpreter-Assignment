import unittest
from validator import Validator


class ValidatorTests(unittest.TestCase):
    global v
    v = Validator()

    def test_id(self):
        self.assertTrue(v.check_id('UY7'))

    def test_gender(self):
        self.assertTrue(v.check_gender('M'))

    def test_age(self):
        pass

    def test_sales(self):
        pass

    def test_bmi(self):
        pass

    def test_salary(self):
        pass

    def test_birthday(self):
        pass

    def test_attributes(self):
        pass

    def test_number_of_attributes(self):
        pass

if __name__  ==" __main__":
    unittest.main()
