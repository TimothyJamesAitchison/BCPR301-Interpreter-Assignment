from __future__ import print_function
import sys


class FileHandler:
    def __init__(self, new_validator):
        self.validator = new_validator

    def open(self, file_path):
        try:
            file = open(file_path, "r")
        except FileNotFoundError:
            print('The file was not found', file=sys.stderr)
            return False
        the_list = []
        for line in file:
            dictionary = {}
            entries = line.split(";")
            for entry in entries:
                if(len(entry.split("=")) == 2):
                    key = entry.split("=")[0]
                    value = entry.split("=")[1]
                    value = value.rstrip('\n')
                    dictionary[key] = value
                else:
                    print('The file was in an invalid format', file=sys.stderr)
                    return False
            the_list.append(dictionary)
        if self.validator.check_data_set(the_list):
            return the_list
        else:
            print("The data in the file failed validation")
            return False