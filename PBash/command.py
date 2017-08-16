import cmd
import string, sys


class Command(cmd.Cmd):
    def __init__(self, new_file_handler, new_view):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.file_handler = new_file_handler
        self.view = new_view

    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self):
        print("syntax: quit",)
        print("-- terminates the application")

    def help_open(self):
        print("syntax: open c:/example/foobar.txt")
        print("-- opens a file from absolute file-path")

    def do_open(self, arg):
        contents = self.file_handler.open(arg)
        if(contents):
            self.view.display(contents)


