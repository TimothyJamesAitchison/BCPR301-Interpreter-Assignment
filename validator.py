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
        if not self.check_bmi(employee_attributes["BMI"]):
            return False
        if not self.check_salary(employee_attributes["SALARY"]):
            return False
        # Failing to invalidate is a success
        return True

    def check_id(self, emp_id):
        if not re.match("[A-Z][0-9]{3}",emp_id):
            print("Invalid Emp Id")
            return False
        else:
            print("Valid Emp Id")
            return True

    def check_age(self, age):
        pass

    def check_sales(self, sales):
        pass

    def check_bmi(self, bmi):
            bmi = bmi.upper()
            body_mass_index = ['NORMAL','OVERWEIGHT','OBESITY','UNDERWEIGHT'];

            for x in body_mass_index:
                if bmi == x:
                 return True

            print('The BMI was invalid', file=sys.stderr)
            return False



    def check_salary(self, salary):
        if not re.match("[0-9]{2,3}",salary):
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
