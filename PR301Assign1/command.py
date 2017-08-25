import cmd
import sys


# noinspection PyUnusedLocal
class Command(cmd.Cmd):
    def __init__(self, new_file_handler, new_db, new_view):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.file_handler = new_file_handler
        self.db = new_db
        self.view = new_view

    @staticmethod
    def do_quit(arg):
        sys.exit(1)

    # Tim
    def help_quit(self):
        print(self.file_handler.open_help('quit'))

    # Tim
    def do_open(self, arg):
        contents = self.file_handler.open(arg)
        if contents:
            self.db.insert(contents)

    # Rosemary
    def help_open(self):
        print(self.file_handler.open_help("open"))

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

    def help_bar(self):
        print(self.file_handler.open_help("bar"))

    # Tim
    def do_get(self, arg):
        self.db.query(arg)

    # Rosemary
    def help_get(self):
        print(self.file_handler.open_help('get'))

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

    # Rosemary
    def help_pie(self):
        print(self.file_handler.open_help('pie'))

    # Hasitha
    def do_line(self, arg):
        sales = self.db.get_data("SALES")
        ages = self.db.get_data("AGE")
        self.view.pygal_line_salebased(sales, ages)

    # Rosemary
    def help_line(self):
        print(self.file_handler.open_help('line'))

    # Rosemary
    def do_linegraph(self, arg):
        ages = self.db.get_data("AGE")
        # print(sales)
        salarys = self.db.get_data("SALARY")
        self.view.age_salary(ages, salarys)

    # Rosemary
    def help_linegraph(self):
        print(self.file_handler.open_help('linegraph'))

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

    def help_scatter(self):
         print(self.file_handler.open_help('scatter'))

    # Tim
    def do_reload(self, arg):
        self.db.load()

    # Rosemary
    def help_reload(self):
        print(self.file_handler.open_help('reload'))
