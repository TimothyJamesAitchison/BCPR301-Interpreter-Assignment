import unittest
from validator import Validator


class ValidatorTests(unittest.TestCase):

    # Rosemary
    def test_id(self):
        v = Validator()
        self.assertFalse(v.check_id('UY7'))
        self.assertFalse(v.check_id('000'))
        self.assertFalse(v.check_id('AAA'))
        self.assertFalse(v.check_id('999'))

    # Rosemary
    def test_gender(self):
        v = Validator()
        # Rosemary
        self.assertTrue(v.check_gender('M'))
        self.assertTrue(v.check_gender('F'))
        # Tim
        self.assertFalse(v.check_gender('m'))
        self.assertFalse(v.check_gender('f'))
        self.assertFalse(v.check_gender(True))
        self.assertFalse(v.check_gender(1))
        self.assertFalse(v.check_gender(None))
        self.assertFalse(v.check_gender({}))
        self.assertFalse(v.check_gender('MF'))

    # Rosemary
    def test_age(self):
        v = Validator()
        self.assertTrue(v.check_age('01'))
        self.assertTrue(v.check_age('99'))

    # Rosemary
    def test_sales(self):
        v = Validator()
        self.assertTrue(v.check_sales('001'))
        self.assertTrue(v.check_sales('999'))
        self.assertFalse(v.check_sales('99'))

    # Tim
    def test_salary(self):
        v = Validator()
        self.assertTrue(v.check_salary('000'))
        self.assertTrue(v.check_salary('001'))
        self.assertTrue(v.check_salary('999'))
        self.assertFalse(v.check_salary(1))
        self.assertFalse(v.check_salary(999))
        self.assertFalse(v.check_salary('1'))
        self.assertFalse(v.check_salary("1000"))
        self.assertFalse(v.check_salary("one"))
        self.assertFalse(v.check_salary(True))

    # Tim
    def test_birthday(self):
        v = Validator()
        self.assertTrue(v.check_birthday('1-1-1996'))
        self.assertTrue(v.check_birthday('31-12-1971'))
        self.assertTrue(v.check_birthday('31-12-1171'))
        self.assertTrue(v.check_birthday('31-12-3171'))
        self.assertFalse(v.check_birthday(56186729))
        self.assertFalse(v.check_birthday('1/1/1996'))
        self.assertFalse(v.check_birthday("Jan-31-1971"))
        self.assertFalse(v.check_birthday(True))
        self.assertFalse(v.check_birthday(""))
        self.assertFalse(v.check_birthday("--"))

    # Tim
    def test_bmi(self):
        v = Validator()
        self.assertTrue(v.check_bmi('Normal'))
        self.assertTrue(v.check_bmi('Overweight'))
        self.assertTrue(v.check_bmi('Obesity'))
        self.assertTrue(v.check_bmi('Underweight'))
        self.assertFalse(v.check_bmi('rUnderweight'))
        self.assertFalse(v.check_bmi('Underweight2'))
        self.assertFalse(v.check_bmi('UNDERWEIGHT'))
        self.assertFalse(v.check_bmi(""))
        self.assertFalse(v.check_bmi(1))
        self.assertFalse(v.check_bmi(True))

    # Tim
    def test_attributes(self):
        v = Validator()
        self.assertTrue(v.check_in_attributes('EMPID'))
        self.assertTrue(v.check_in_attributes('GENDER'))
        self.assertTrue(v.check_in_attributes('AGE'))
        self.assertTrue(v.check_in_attributes('SALES'))
        self.assertTrue(v.check_in_attributes('BMI'))
        self.assertTrue(v.check_in_attributes('SALARY'))
        self.assertTrue(v.check_in_attributes("BIRTHDAY"))
        self.assertTrue(v.check_in_attributes("birthday"))
        self.assertFalse(v.check_in_attributes(True))
        self.assertFalse(v.check_in_attributes(['EMPID', 'GENDER']))
        self.assertFalse(v.check_in_attributes(None))
        self.assertFalse(v.check_in_attributes(1))

suite = unittest.TestLoader().loadTestsFromTestCase(ValidatorTests)
unittest.TextTestRunner(verbosity=1).run(suite)
