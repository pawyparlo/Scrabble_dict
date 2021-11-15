from database import Database
import random

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
        self.letters = self.collect_letters()
        return self.letters

    def listContainer(self):
        self.list = []
        return self.list

    def listPermutation(self, a, size):
        '''Based on heaps permutation'''
        # if size becomes 1 then prints the obtained
        # permutation
        if size == 1:
            self.list.append(a) # print here if needed
            return
            
        for i in range(size):
            self.listPermutation(a, size-1)
    
            # if size is odd, swap 0th i.e (first)
            # and (size-1)th i.e (last) element
            # else If size is even, swap ith
            # and (size-1)th i.e (last) element
            if size & 1:
                a[0], a[size-1] = a[size-1], a[0]
            else:
                a[i], a[size-1] = a[size-1], a[i]

    def listPop(self, n):
        '''Pick up n random letters from list'''
        assert n > 2, f'number can\'t be smaller than 2'
        current_list = self.collect_letters()
        random.shuffle(current_list)

        if len(current_list) >= 2:
            for i in range(n):
                try:
                    current_list.pop()
                except:
                    print(f'List is empty!')
            return current_list
        else:
            print(f'Min. list items is 2, current nr of items {len(current_list)}')
            return
    
    def createWord(self, letter_list):
        'Methdo provided to convert list of letters to string'
        word = ''
        for letters in letter_list:
            word += letters
        print(word)
        return word


    def printResult(self, word):
        result = [] # Results container

        for words in self.content_list:
            if word in words:
                result.append(words)
        return result
    





Data = DataContainer('list_of_words_pl.txt')
Data.read_content()
Data.process_data()
Data.find_word()
Data.listContainer()
letters = Data.listPop()
word = Data.createWord(letters)
print(Data.printResult(word))

# Data.listPop()

#Data.listPermutation(Data.find_word(), len(Data.find_word()))
# print(Data.list)

