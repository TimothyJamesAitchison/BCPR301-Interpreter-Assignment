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

    def do_reload(self, arg):
        self.db.load()
