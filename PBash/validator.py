from __future__ import print_function
import sys


class Validator:
    def __init__(self):
        self.id_rule = "[A-Z][0-9]{3}"
        self.gender_rule = "(M|F)"
        self.age_rule = "[0-9]{2}"
        self.sales_rule =  "[0-9]{3}"
        self.bmi_rule = "(Normal|Overweight|Obesity|Underweight)"
        self.salary_rule = "[0-9]{2,3}"
        self.birthday_rule = "[1-31]-[1-12]-[0-9]{4}"
        self.attributes = {"ID", "GENDER", "AGE", "SALES", "BMI", "SALARY", "BIRTHDAY"}
        self.number_of_attributes = len(self.attributes)

    def check_data_set(self, data_set):
        # Should be of form [{EMPID: B12, GENDER: M, AGE: 22, etc}, {EMPID: 55Y, GENDER: F, etc}]
        if len(data_set) == 0:
            print('The data was empty', file=sys.stderr)
            return False
        else:
            for employee in data_set:
                if not self.check_line(employee):
                    print('One or more of the lines of data was invalid', file=sys.stderr)
                    return False
        # Failing to invalidate is a success
        return True

    def check_line(self, employee_attributes):
        # Should be of form {EMPID: B12, GENDER: M, AGE: 22, etc}
        for attribute in self.attributes:
            if attribute not in employee_attributes:
                print('Missing attribute: {}'.format(attribute), file=sys.stderr)
                return False
        # Failing to invalidate is a success
        return True

    def check_id(self):
        pass

    def check_age(self):
        pass

    def check_sales(self):
        pass

    def check_bmi(self):
        pass

    def check_salary(self):
        pass

    def check_birthday(self):
        pass
