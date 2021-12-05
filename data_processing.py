from database import Database
from string import ascii_lowercase


class DataContainer(Database):
    def __init__(self, filename = 'list_of_words_pl.txt'):
        super().__init__()
        self.filename = filename
        self.file = open(self.filename, 'r')
        self.__readContent()
        self.permutation_list = [] # list of permutations as list of strings

    def __readContent(self):
        self.content = self.file.read()
        #self.content = self.content.splitlines()

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

    def listPop(self):

        if len(self.collectLetters()) < 3:

            self.listPermutation(self.collectLetters(), len(self.collectLetters()))

            for permutations in self.permutation_list:
                word = self.createWord(permutations)

                for words in self.content.splitlines():

                    if word == words:
                        print(words)

        elif len(self.collectLetters()) >= 3:
            
            letters = self.collectLetters()

            while len(letters) != 0:

                self.listPermutation(letters, len(letters))

                for permutations in self.permutation_list:
                    word = self.createWord(permutations)

                    for words in self.content.splitlines():

                        if word == words:
                            print(words)

                letters.pop()
                self.permutation_list.clear()   

                letters = self.removeLetter(letters)      

    def binarySearch(self, word):
        
        self.book = self.content.splitlines() # List of words to iterate
        self.alphabet = list(ascii_lowercase)

        start = 0
        end = len(self.book) - 1

        while start <= end:

            middle = (start + end)// 2
            midpoint = self.book[middle]
            
            if self.alphabet.index(midpoint[0]) > self.alphabet.index(word[0]):
                end = middle - 1
                
            elif self.alphabet.index(midpoint[0]) < self.alphabet.index(word[0]):
                start = middle + 1
                
            elif midpoint[0] == word[0]:
                return self.book.index(midpoint)



    def createWord(self, permutation):
        word = ''

        for letter in permutation:
            if letter.isalpha():
                word += letter

        return word

    def removeLetter(self, letters):
        
        if len(letters) < 1:
            return []

        else:

            try:

                for i in range(0,len(letters)):
                    if i == 0:
                        return letters[i + 1:len(letters)]
                        
                    elif i != len(letters) - 1:
                        return letters[0:i] + letters[i + 1:len(letters)]

                    else:
                        return letters[0:i]  

            except IndexError:
                pass

  


