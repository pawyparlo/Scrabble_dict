from database import Database
import random


class DataContainer(Database):
    def __init__(self, filename = 'list_of_words_pl.txt'):
        super().__init__()
        self.filename = filename
        self.file = open(self.filename, 'r')
        self.permutation_list = []

    def __readContent(self):
        self.content = self.file.read()
        self.content = self.content.splitlines()

    # def listContainer(self):
    #     self.list = []
    #     return self.list

    def listPermutation(self, a, size):
        '''Based on Heap's permutation'''
        if size == 1:
            self.permutation_list.append(str(a)) 
            return 
            
        for i in range(size):
            self.listPermutation(a, size-1)
    
            if size & 1: # bitwise operation - return 0/1
                a[0], a[size-1] = a[size-1], a[0]

            else:
                a[i], a[size-1] = a[size-1], a[i]


    def listPop(self, n):
        '''Pick up n random letters from list'''
        assert n >= 2, f'Number of letters can\'t be smaller than 2'
        current_list = self.collectLetters()
        random.shuffle(current_list)

        if len(current_list) >= 2:
            for i in range(n):
                try:
                    current_list.pop()
                except:
                    print(f'List is empty!, list state {current_list}')
            return current_list

        else:
            print(f'Min. list items is 2, current nr of items {len(current_list)}')
            return
    
    def createWord(self, letter_list):
        return ''.join(letter_list)

    def printResult(self):
        return [word for word in self.collectLetters()]



