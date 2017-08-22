class View:
    def display(self, list_of_dictionaries):
        for dictionary in list_of_dictionaries:
            for key in dictionary:
                print("{0} = {1}".format(key, dictionary[key]))
