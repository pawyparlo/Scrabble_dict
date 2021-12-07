# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from database import Database
import codecs


class DataContainer(Database):
    def __init__(self, filename = 'list_of_words_pl.txt'):
        super().__init__()
        self.filename = filename
        self.file = codecs.open(self.filename, 'r', 'utf-8') # Necessary to read polish letters
        self.__readContent()
        self.permutation_list = list()
        self.permutation_set = set() 

    def __readContent(self):
        self.content = self.file.read()

    def hashMapData(self):
        '''Method assigning as key alphabet_letter to values,
            which are words starting by this letter'''
        self.hashLetters = dict()

        for word in self.content.splitlines():
            if word[0] not in self.hashLetters:
                self.hashLetters[word[0]]=[word]  
                      
            elif word[0] in self.hashLetters:
                self.hashLetters[word[0]].append(word)

    def setData(self):
        '''Method storing data into set'''
        self.setLetters = set(self.content.splitlines())

    def permutationsToList(self, a: list, size: int):
        '''Algorithm based on Heap's permutation,
            Create permutations with given letters'''
        if size == 1:
            self.permutation_list.append(''.join(a))
            return 
            
        for i in range(size):
            self.permutationsToList(a, size-1)
            if size & 1: # bitwise operation - return 0/1
                a[0], a[size-1] = a[size-1], a[0]

            else:
                a[i], a[size-1] = a[size-1], a[i]

    def permutationsToSet(self, a: set, size: int):
        '''Algorithm based on Heap's permutation,
            Create permutations with given letters'''
        if size == 1:
            self.permutation_set.add(''.join(a)) 
            return 
            
        for i in range(size):
            self.permutationsToSet(a, size-1)
            if size & 1: # bitwise operation - return 0/1
                a[0], a[size-1] = a[size-1], a[0]

            else:
                a[i], a[size-1] = a[size-1], a[i]


