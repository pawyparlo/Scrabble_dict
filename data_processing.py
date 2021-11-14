from database import Database

class DataContainer(Database):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

        self.file = open(self.filename, 'r')

    def read_content(self):
        self.content = self.file.read()
        # Content read

    def process_data(self):
        self.content_list = self.content.splitlines()

    def find_word(self):
        result = []
        letters = self.collect_letters()
        # WWWW
        string = ''
        for x in letters:
            string += x
        for words in self.content_list:
            if string in words:
                result.append(words) 
        print(result)


Data = DataContainer('list_of_words_pl.txt')
Data.read_content()
Data.process_data()
Data.find_word()