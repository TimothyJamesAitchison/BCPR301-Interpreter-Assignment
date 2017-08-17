from command import Command
from file_handler import FileHandler
from validator import Validator
from view import View
from db import DatabaseHandler

cli = Command(FileHandler(Validator()), DatabaseHandler(Validator()), View())
cli.cmdloop()
