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
	# Hasitha	
		self.assertFalse(v.check_age('5'))
        self.assertFalse(v.check_age('100'))
		self.assertFalse(v.check_age('100'))

    # Rosemary
    def test_sales(self):
        v = Validator()
        self.assertTrue(v.check_sales('001'))
        self.assertTrue(v.check_sales('999'))
        self.assertFalse(v.check_sales('99'))
	# Hasitha	
		self.assertFalse(v.check_sales('-996'))
        self.assertFalse(v.check_sales('9999+'))
		self.assertTrue(v.check_sales('123'))
		self.assertTrue(v.check_sales('010'))

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
	# Hasitha	
		self.assertFalse(v.check_salary('$120'))
        self.assertFalse(v.check_salary("1000+200+300$"))
        self.assertFalse(v.check_salary("five hundred dollar"))
       
		

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
	# Hasitha	
		self.assertFalse(v.check_birthday('31/02/1996'))
        self.assertFalse(v.check_birthday("ap;r;-31-1971"))
        self.assertFalse(v.check_birthday("noValidate"))
        self.assertFalse(v.check_birthday("no answer"))
        self.assertFalse(v.check_birthday(31/02/2016))
		self.assertFalse(v.check_birthday(Today))
		

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
	# Hasitha	
		self.assertFalse(v.check_bmi('under_weight'))
        self.assertFalse(v.check_bmi('uderweight'))
        self.assertFalse(v.check_bmi("NoRmal"))
        self.assertFalse(v.check_bmi(n2))
        self.assertFalse(v.check_bmi(nw))

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
