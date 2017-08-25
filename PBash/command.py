import cmd
import sys


class Command(cmd.Cmd):
    def __init__(self, new_file_handler, new_db, new_view):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.file_handler = new_file_handler
        self.db = new_db
        self.view = new_view

    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self):
        print("syntax: quit",)
        print("-- terminates the application")

    def help_open(self):
        print(self.file_handler.open_help("OPEN"))
        print("syntax: open c:/example/foobar.txt")
        print("-- opens a file from absolute file-path")

    def do_open(self, arg):
        contents = self.file_handler.open(arg)
        if contents:
            self.db.insert(contents)

    def do_bar(self, arg):
        if self.db.get_data(arg):
            self.view.plot_bar(self.db.get_data(arg), arg)

    def do_test(self, arg):
        contents = self.file_handler.open("c:/testfile/file.txt")
        if contents:
            self.view.display(contents)
            self.db.insert(contents)

    def do_get(self, arg):
        self.db.query(arg)

    def do_pie(self, arg):
        arg = arg.upper()
        if arg == "GENDER":
            if self.db.get_data(arg):
                self.view.plot_pie_gender(self.db.get_data(arg))
    # hasitha
    def do_line(self,arg):
        sales = self.db.get_data("SALES")
        #print(sales)
        ages = self.db.get_data("AGE")
        self.view.pygal_line_salebased(sales,ages)

    def do_reload(self, arg):
        self.db.load()

    # Rosemary
    def do_search(self, arg):
        emp_info = self.db.get_emp()
        print(emp_info)

    def help_search(sef):
    	print("Search an employee's information by ID")

    def do_linegraph(self,arg):
        ages = self.db.get_data("AGE")
        #print(sales)
        salarys = self.db.get_data("SALARY")
        self.view.pygal_line_salebased(ages,salarys)
