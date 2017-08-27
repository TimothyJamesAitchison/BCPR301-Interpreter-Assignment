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

    # Rosemary
    def help_quit(self):
        result = self.file_handler.open_help("quit")
        if result == "No such command.":
            print("Could not find entry in help file")
        else:
            print(result)

    # Tim
    def do_open(self, arg):
        contents = self.file_handler.open(arg)
        if contents:
            self.db.insert(contents)

    # Tim
    def help_open(self):
        result = self.file_handler.open_help("open")
        if result == "No such command.":
            print("Could not find entry in help file")
        else:
            print(result)

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

    # Tim
    def help_get(self):
        result = self.file_handler.open_help("get")
        if result == "No such command.":
            print("Could not find entry in help file")
        else:
            print(result)

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

    # Tim
    def help_pie(self):
        result = self.file_handler.open_help("pie")
        if result == "No such command.":
            print("Could not find entry in help file")
        else:
            print(result)

    # Hasitha
    def do_line(self, arg):
        sales = self.db.get_data("SALES")
        ages = self.db.get_data("AGE")
        self.view.pygal_line_salebased(sales, ages)

    # Tim
    def help_line(self):
        result = self.file_handler.open_help("line")
        if result == "No such command.":
            print("Could not find entry in help file")
        else:
            print(result)

    # Rosemary
    def do_linegraph(self, arg):
        ages = self.db.get_data("AGE")
        # print(sales)
        salarys = self.db.get_data("SALARY")
        self.view.age_salary(ages, salarys)

    # Tim
    def help_linegraph(self):
        result = self.file_handler.open_help("linegraph")
        if result == "No such command.":
            print("Could not find entry in help file")
        else:
            print(result)

    # Tim
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

    #Rosemary
    def help_scatter(self):
        result = self.file_handler.open_help("scatter")
        if result == "No such command.":
            print("Could not find entry in help file")
        else:
            print(result)

    # Tim
    def do_reload(self, arg):
        self.db.load()
        self.file_handler.set_rules()

    # Hasitha
    def help_reload(self):
        result = self.file_handler.open_help("reload")
        if result == "No such command.":
            print("Could not find entry in help file")
        else:
            print(result)
