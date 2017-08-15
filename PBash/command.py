import cmd
import string, sys


class Command(cmd.Cmd):
    def __init__(self, file_handler):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.file_handler = file_handler

    def do_hello(self, arg):
        print("hello again", arg, "!")

    def help_hello(self):
        print("-- prints a hello message")

    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self):
        print("syntax: quit",)
        print("-- terminates the application")

    def help_open(self):
        print("opens a file")

    def do_open(self, arg):
        self.file_handler.open(arg)


