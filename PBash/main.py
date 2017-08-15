from command import Command
from file_handler import FileHandler
from validator import Validator

cli = Command(FileHandler(), Validator())
cli.cmdloop()
