"""import csv
import os


class ExcelParser:

    def csv_dict_reader(self, file_obj):
        reader = csv.DictReader(file_obj, delimiter=',')
        for line in reader:
            print(line["emp_id"])
            print(line["gender"])
            print(line["sales"])
            print(line["bmi"])
            print(line["salary"])
            print(line["birthday"])

    def csv_open(self):
        try:
            with open("data.csv") as f_obj:
               data.csv_dict_reader(f_obj)
        except FileExistsError:
            print("file doesnt found")

data = ExcelParser()
data.csv_open()
# data.csv_dict_reader()
"""
l = ['element1\t0238.94', 'element2\t2.3904', 'element3\t0139847']
print([i.split('\t', 1)[0] for i in l])
