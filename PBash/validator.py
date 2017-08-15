class Validator:
    def __init__(self):
        self.id_rule = "[A-Z][0-9]{3}"
        self.gender_rule = "(M|F)"
        self.age_rule = "[0-9]{2}"
        self.sales_rule =  "[0-9]{3}"
        self.bmi_rule = "(Normal|Overweight|Obesity|Underweight)"
        self.salary_rule = "[0-9]{2,3}"
        self.birthday_rule = "[1-31]-[1-12]-[0-9]{4}"

    def check_data_set(self):
        # Should be of form [{EMPID: B12, GENDER: M, AGE: 22, etc}, {EMPID: 55Y, GENDER: F, etc}]
        pass

    def check_line(self):
        # Should be of form {EMPID: B12, GENDER: M, AGE: 22, etc}
        pass

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
