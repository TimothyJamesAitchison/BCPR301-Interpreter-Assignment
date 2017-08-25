from __future__ import print_function
import sys
import csv
import re
from validator import Validator


class FileHandler:
    def __init__(self, new_validator):
        self.validator = new_validator

    def open(self, file_path):
        if re.search(r'\.csv$', file_path):
            return self.csv_dict_reader(file_path)
        elif re.search(r'\.txt$', file_path):
            return self.txt_dict_reader(file_path)
        else:
            print('Invalid file extension', file=sys.stderr)
            return False

    def txt_dict_reader(self, filename):
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print('The file was not found', file=sys.stderr)
            return False
        the_list = []
        for line in file:
            dictionary = {}
            entries = line.split(";")
            for entry in entries:
                if len(entry.split("=")) == 2:
                    key = entry.split("=")[0]
                    value = entry.split("=")[1]
                    value = value.rstrip('\n')
                    dictionary[key] = value
                else:
                    print('The file was in an invalid format', file=sys.stderr)
                    return False
            if self.validator.check_line(dictionary):
                the_list.append(dictionary)
            else:
                print('Entry failed validation', file=sys.stderr)
        if self.validator.check_data_set(the_list):
            return the_list
        else:
            print("There were no valid entries in the file", file=sys.stderr)
            return False

    #hasitha
    def csv_dict_reader(self, filename):
        """
        >>> f = FileHandler(Validator())
        >>> result = f.csv_dict_reader("data.csv")
        >>> print(result[0]['EMPID'])
        A001
        >>> print(result[0]['GENDER'])
        F
        >>> print(result[0]['AGE'])
        21
        >>> print(result[0]['SALES'])
        001
        >>> print(result[0]['BMI'])
        Normal
        >>> print(result[0]['BIRTHDAY'])
        1-1-1996
        >>> print(result[0]['SALARY'])
        12
        """
        try:
            with open(filename) as f_obj:
                reader = csv.DictReader(f_obj, delimiter=',')
                the_list = []
                for line in reader:
                    employee = dict()
                    employee["EMPID"] = line["emp_id"]
                    employee["GENDER"] = line["gender"]
                    employee["AGE"] = line["age"]
                    employee["SALES"] = line["sales"]
                    employee["BMI"] = line["bmi"]
                    employee["SALARY"] = line["salary"]
                    employee["BIRTHDAY"] = line["birthday"]

                    if self.validator.check_line(employee):
                        the_list.append(employee)
                    else:
                        print('Entry failed validation', file=sys.stderr)
                        for key in employee:
                            print(key)
                            print(employee[key])
                if self.validator.check_data_set(the_list):
                    return the_list
                else:
                    print("There were no valid entries in the file", file=sys.stderr)
                    return False
        except FileNotFoundError:
            print('The file was not found', file=sys.stderr)
            return False

    def open_help(self, subject):
        pass
        # open the file (hard-coded file path)
        # split the file into entries
        # check the entries for the subject
        # if found, return the result for that subject

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=0)
