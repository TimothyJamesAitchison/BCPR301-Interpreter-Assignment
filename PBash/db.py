import sqlite3


class DatabaseHandler:
    def __init__(self, new_validator, database):
        self.validator = new_validator
        self.database = database

        try:
            self._connection = sqlite3.connect(database + ".db")
            self._cursor = self._connection.cursor()
            self.close_db()
        except Exception as e:
            print(e)

    def load(self):
        try:
            self.destroy_db()
            self.build_db()
        except Exception as e:
            print(e)
        else:
            print("Opened database successfully")
        finally:
            print("Finishing connecting to database")

    def open_db(self):
        try:
            self._connection = sqlite3.connect(self.database + ".db")
            self._cursor = self._connection.cursor()
        except Exception as e:
            print(e)

    def destroy_db(self):
        self.open_db()
        self._cursor.execute("""DROP TABLE IF EXISTS employee;""")
        self.close_db()

    def build_db(self):
        self.open_db()
        sql_command = """
        CREATE TABLE employee (
        empid VARCHAR(20) PRIMARY KEY,
        gender CHAR(1),
        age INTEGER,
        sales INTEGER,
        bmi VARCHAR(20),
        salary INTEGER,
        birthday DATE);"""
        try:
            self._cursor.execute(sql_command)
        except Exception as e:
            print(e)
        else:
            self._connection.commit()
        self.close_db()

    def close_db(self):
        self._connection.close()

    def insert(self, employees):
        self.open_db()
        for employee in employees:
            format_str = """INSERT INTO employee (empid, gender, age, sales, bmi, salary, birthday)
                VALUES ("{empid}", "{gender}", "{age}", "{sales}", "{bmi}", "{salary}", "{birthday}");"""
            sql_command = format_str.format(
                empid=employee["EMPID"],
                gender=employee["GENDER"],
                age=employee["AGE"],
                sales=employee["SALES"],
                bmi=employee["BMI"],
                salary=employee["SALARY"],
                birthday=employee["BIRTHDAY"])
            try:
                self._cursor.execute(sql_command)
            except Exception as e:
                print(e)
            else:
                print("Successfully added employee {0} to database".format(employee["EMPID"]))
                self._connection.commit()
        self.close_db()

    def query(self, emp_id):
        self.open_db()
        sql_result = self._cursor.execute('SELECT * FROM employee WHERE empid = "{empid}"'.format(empid=emp_id))
        employee = sql_result.fetchone()
        if employee:
            print(employee)
        else:
            print("No such employee found")
        self.close_db()

    def get_data(self, field):
        self.open_db()
        if not self.validator.check_in_attributes(field):
            return False
        else:
            sql_result = self._cursor.execute('SELECT EMPID, {field} FROM employee'.format(field=field))
            employees = sql_result.fetchall()
            self.close_db()
            return employees
