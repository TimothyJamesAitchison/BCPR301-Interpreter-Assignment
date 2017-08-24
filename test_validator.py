import unittest
from validator import Validator


class ValidatorTests(unittest.TestCase):
    # for good day scenarios
    global v
    v = Validator()

    def test_id(self):
        self.assertTrue(v.check_id('UY7'))
        self.assertTrue(v.check_id('000'))
        self.assertTrue(v.check_id('AAA'))
        self.assertTrue(v.check_id('999'))

    def test_gender(self):
        self.assertTrue(v.check_gender('M'))
        self.assertTrue(v.check_gender('F'))

    def test_age(self):
        self.assertTrue(v.check_age(1))
        self.assertTrue(v.check_age(99))

    def test_sales(self):
        self.assertTrue(v.check_sales(1))
        self.assertTrue(v.check_sales(99))
        self.assertTrue(v.check_sales(998))
    #hasitha
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
