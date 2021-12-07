from database import Database
from data_storage import DataContainer
from math import factorial
from time import time
from string import ascii_lowercase, ascii_uppercase
from random import choice

polish_letters = ['a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k',
                  'l','ł','m','n','ń','o','ó','p','q','r','s','ś','t','u',
                  'v','w','x','y','z','ź','ż']

english_letters = list(ascii_uppercase) #TXT file is given with uppercase letters


# class DataProcessingTests(DataContainer):
#     def __init__(self):
#         super().__init__()
#         self.objectname = DataContainer()
#         self.__colectPermutations()

#     def tryCreateObject(self):
#         return self.objectname != None

#     def tryCollectLletters(self):
#         return self.collectLetters() != None

#     def __colectPermutations(self):
#         self.objectname.listPermutation(self.collectLetters(),len(self.collectLetters()))
#         self.permutations = self.objectname.permutation_list

#     def tryToPermuteList(self):
#         var = self.collectLetters()
#         return len(self.permutations) == factorial(len(var))

#     def tryPrintPermutations(self):
#         for i in range(0, len(self.permutations), 3):
#             try:
#                 print(self.permutations[i],
#                       self.permutations[i+1],
#                       self.permutations[i+2])
#             except IndexError:
#                 pass

#     def tryPrintletters(self):
#         return self.collectLetters()

#     def main_function(self):

#         return self.listPop()

#     def __repr__(self):
#         return 


# class DataBaseTests(Database):
#     def __init__(self):
#         super().__init__()
#         self.objectname = Database

#     def tryCreatetable(self):
#         if self.objectname != None:
#             return True
#         else:
#             return False





# class AlgorithmTests(DataProcessingTests):
#     def __init__(self, list_input: list):
#         super().__init__()
#         self.list_input = list_input

#     def listPop(self): 
#         '''Overwritted method in reason to create list with variable
#             length and then count its time running'''

#         if len(self.list_input) < 3:
    
#             self.listPermutation(self.list_input, len(self.list_input))
            
        
#             for permutations in self.permutation_list:

#                 word = self.createWord(permutations)

#                 for i in self.hashLetters[word[0]]:

#                     if i == word:
#                         print(i)

                
#         elif len(self.list_input) >= 3:
            
#             letters = self.list_input

#             while len(letters) != 0:


#                 self.listPermutation(letters, len(letters))


#                 for permutations in self.permutation_list:
                    
#                     word = self.createWord(permutations)

#                     for i in self.hashLetters[word[0]]:

#                         if word == i:
#                             print(i)

#                 letters.pop()
#                 self.permutation_list.clear()   

#                 letters = self.removeLetter(letters)  





# def test_algorithm_time():

#     strings = polish_letters
#     timelapse = []
#     for i in range(7, 1, -1):
#         random_letters = [choice(strings) for x in range(0,i)]
#         print(random_letters)
#         start = time()
#         test = AlgorithmTests(list_input=random_letters)
#         test.hashData()
#         test.main_function()
#         end = time()
#         timelapse.append((end-start, f'nr of letters {i}'))

#     for i in timelapse:
#         print(i)

# test_algorithm_time()

# def test_hashData():
#     object=DataContainer()
#     start=time()
#     object.hashData()
#     end=time()
#     print(f'Time spent: {end-start}')
#     print(len(object.hashData))
#     print(object.hashData['A'])

# # test_hashData()