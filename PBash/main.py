from command import Command
from file_handler import FileHandler
from validator import Validator
from view import View

cli = Command(FileHandler(Validator()), View())
cli.cmdloop()
