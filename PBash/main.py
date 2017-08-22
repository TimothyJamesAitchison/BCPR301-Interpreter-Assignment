from command import Command
from file_handler import FileHandler
from validator import Validator
from view import View
from db import DatabaseHandler
import pickle

try:
    database = pickle.load( open( "db.p", "rb" ) )
except FileExistsError:
    database = DatabaseHandler(Validator())
    database.load()
    pickle.dump(database, open("db.p", "wb"))
cli = Command(FileHandler(Validator()), database, View())
cli.cmdloop()
