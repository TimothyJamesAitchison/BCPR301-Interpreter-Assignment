from __future__ import print_function
import sys
from abc import ABCMeta, abstractmethod
import re
import datetime as date


class IFileValidator(metaclass=ABCMeta):
    @abstractmethod
    def check_data_set(self, data_set):
        pass

    @abstractmethod
    def check_line(self, employee_attributes):
        pass

    @abstractmethod
    def check_id(self, emp_id):
        pass

    @abstractmethod
    def check_age(self, age):
        pass

    @abstractmethod
    def check_sales(self, sales):
        pass

    @abstractmethod
    def check_bmi(self, bmi):
        pass

    @abstractmethod
    def check_salary(self, salary):
        pass

    @abstractmethod
    def check_birthday(self, birthday):
        pass

    @abstractmethod
    def check_birthday_against_age(self, birthday, age):
        pass


class Validator(IFileValidator):

    def __init__(self):
        self.id_rule = "[A-Z][0-9]{3}"
        self.gender_rule = "(M|F)"
        self.age_rule = "[0-9]{2}"
        self.sales_rule =  "[0-9]{3}"
        self.bmi_rule = "(Normal|Overweight|Obesity|Underweight)"
        self.salary_rule = "[0-9]{2,3}"
        self.birthday_rule = "[1-31]-[1-12]-[0-9]{4}"
        self.attributes = {"EMPID", "GENDER", "AGE", "SALES", "BMI", "SALARY", "BIRTHDAY"}
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
        if not self.check_birthday(employee_attributes["BIRTHDAY"]):
            return False
        # Failing to invalidate is a success
        return True

    def check_id(self, emp_id):
        # Should be in form of [A-Z][0-9]{3}
        if len(emp_id) != 3:
            print('The length of employeeID is invalid!', file=sys.stderr)
            return False
        else:
            if emp_id.islower():
                print('The format of employeeID is invalid!', file=sys.stderr)
                return False
        # Failing to invalidate is a success
        return True
    def check_gender(self,gender):
        sex = ['M', 'F']
        if gender in sex:
            return  True
        else:
            return  False

    def check_age(self, age):
        # Should be between 1-99
        if age not in range(1,100):
            print('Invalid age!')
            return False
        # Failing to invalidate is a success
        return True

    def check_sales(self, sales):
        if sales not in range(1,999):
            print('Valid sales!')
            return True
        # Failing to invalidate is a success
        return False

    def check_bmi(self, bmi):
        bmi = bmi.upper()
        body_mass_index = ['NORMAL', 'OVERWEIGHT', 'OBESITY', 'UNDERWEIGHT'];

        for x in body_mass_index:
            if bmi == x:
                return True

        print('The BMI was invalid', file=sys.stderr)
        return False

    def check_salary(self, salary):
        if not re.match("[0-9]{2,3}", salary):
            print("Invalid salary")
            return False
        else:
            print("Valid salary")
            return True


    def check_birthday(self, birthday):
        try:
            day_month_year = birthday.split("-")
            day = int(day_month_year[0])
            month = int(day_month_year[1])
            year = int(day_month_year[2])
            date.datetime(year, month, day)
            return True
        except ValueError:
            print('The date was invalid', file=sys.stderr)
            return False

    def check_birthday_against_age(self, birthday, age):
        pass

    def check_in_attributes(self, query_attribute):
        """
        >>> v = Validator()
        >>> v.check_in_attributes("EMPID")
        True
        >>> v.check_in_attributes("GENDER")
        True
        >>> v.check_in_attributes("AGE")
        True
        >>> v.check_in_attributes("SALES")
        True
        >>> v.check_in_attributes("BMI")
        True
        >>> v.check_in_attributes("SALARY")
        True
        >>> v.check_in_attributes("BIRTHDAY")
        True
        >>> v.check_in_attributes("Salary")
        True
        >>> v.check_in_attributes("SALE")
        False
        >>> v.check_in_attributes(True)
        False
        >>> v.check_in_attributes(False)
        False
        >>> v.check_in_attributes(1)
        False
        """
        try:
            return query_attribute.upper() in self.attributes
        except AttributeError:
            return False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=1)