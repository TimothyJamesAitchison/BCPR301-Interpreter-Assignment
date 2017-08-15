class FileHandler:
    def open(self, file_path):
        file = open(file_path, "r")
        for line in file:
            print(line)