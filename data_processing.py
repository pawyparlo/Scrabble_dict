
class DataContainer():
    def __init__(self, filename):
        self.filename = filename

        self.file = open(self.filename, 'r')

    def read_content(self):
        self.content = self.file.read()
        # Content read

    def __process_data(self):
        self.content_list = self.content.splitlines()

    def find_word(self):
        pass

Data = DataContainer('list_of_words_pl.txt')
Data.read_content()
Data.process_data()