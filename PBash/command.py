import cmd
import sys


class Command(cmd.Cmd):
    def __init__(self, new_file_handler, new_db, new_view):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.file_handler = new_file_handler
        self.db = new_db
        self.view = new_view

    @staticmethod
    def do_quit(self):
        sys.exit(1)

    def help_quit(self):
        pass

    # Tim
    def do_open(self, arg):
        contents = self.file_handler.open(arg)
        if contents:
            self.db.insert(contents)

    # ???
    def help_open(self):
        print(self.file_handler.open_help("OPEN"))

    # Tim
    def do_bar(self, arg):
        arg = arg.upper()
        if arg in ("SALES", "SALARY", "AGE"):
            if self.db.get_data(arg):
                self.view.plot_bar(self.db.get_data(arg))
            else:
                print("Couldn't find valid data")
        else:
            print('The valid options for a bar graph are sales, salary or age')

    # Tim
    def do_get(self, arg):
        self.db.query(arg)

    # ???
    def help_get(self):
        pass

    # Tim
    def do_pie(self, arg):
        arg = arg.upper()
        if arg == "GENDER":
            if self.db.get_data(arg):
                self.view.plot_pie_gender(self.db.get_data(arg))
            else:
                print("Couldn't find valid data")
        else:
            print('The valid option for a pie graph is currently only gender')

    # ???
    def help_pie(self):
        pass

    # Hasitha
    def do_line(self, arg):
        sales = self.db.get_data("SALES")
        ages = self.db.get_data("AGE")
        self.view.pygal_line_salebased(sales,ages)

    # ???
    def help_line(self):
        pass

    # Rosemary
    def do_linegraph(self, arg):
        ages = self.db.get_data("AGE")
        # print(sales)
        salarys = self.db.get_data("SALARY")
        self.view.age_salary(ages, salarys)

    # ???
    def help_linegraph(self):
        pass

    def do_scatter(self, arg):
        arg = arg.upper()
        if arg == "SALARY":
            salary = self.db.get_data("SALARY")
            age = self.db.get_data("AGE")
            self.view.age_salary(age, salary)
        elif arg == "SALES":
            sales = self.db.get_data("SALES")
            age = self.db.get_data("AGE")
            self.view.pygal_line_salebased(sales, age)
        else:
            print('The valid options for a scatter graph are salary or sales')

    # Tim
    def do_reload(self, arg):
        self.db.load()

    # ???
    def help_reload(self):
        pass