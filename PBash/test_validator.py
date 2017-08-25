import unittest
from validator import Validator


class ValidatorTests(unittest.TestCase):
    # for good day scenarios
    # Rosemary

    # Rosemary
    def test_id(self):
        v = Validator()
        self.assertTrue(v.check_id('UY7'))
        self.assertTrue(v.check_id('000'))
        self.assertTrue(v.check_id('AAA'))
        self.assertTrue(v.check_id('999'))

    # Rosemary
    def test_gender(self):
        v = Validator()
        self.assertTrue(v.check_gender('M'))
        self.assertTrue(v.check_gender('F'))

    # Rosemary
    def test_age(self):
        v = Validator()
        self.assertTrue(v.check_age(1))
        self.assertTrue(v.check_age(99))

    # Rosemary
    def test_sales(self):
        v = Validator()
        self.assertTrue(v.check_sales(1))
        self.assertTrue(v.check_sales(99))
        self.assertTrue(v.check_sales(998))

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

# Rosemary
if __name__ == "__main__":
    unittest.main()
