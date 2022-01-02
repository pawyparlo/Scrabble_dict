from itertools import permutations
from collections import defaultdict

from time import time


class BestPermutationAlgorithm:

    def __init__(self, word):
        self.container = defaultdict(list)

        self.word = list(word)

        print(self.itertoolsPermutations(self.word))
        print(self.recursionPermutations(self.word))
        print(self.recursionHeapsPermutation(len(self.word), self.word))
        print(self.recursionBacktrackingPermutation(len(self.word), self.word))
        print(self.lexicoGraphicPermutation(self.word))

    def __testTime(func):
        
        def inside_wrapper(self, *args, **kwargs):
            start_time = time()
            func(self, *args, **kwargs)
            word_len = len(self.container[func.__name__])
            end_time = time()

            return (f'Algorithm: {func.__name__} \n time: {(end_time-start_time):.8f} \n nr of permutations: {word_len}')
        return inside_wrapper

    @__testTime
    def itertoolsPermutations(self, word: list):
        # result = [''.join(x) for x in permutations(word)]
        for x in permutations(word):
            self.container['itertoolsPermutations'].append(''.join(x))
        

    @__testTime
    def recursionPermutations(self, word: list, step: int=0):
        if step==len(word):
            self.container['recursionPermutations'].append(''.join(word))

        for i in range(step, len(word)):
            string_copy = word
            string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

            self.recursionPermutations(string_copy, step+1)

    @__testTime
    def recursionHeapsPermutation(self, size: int, word: list):
        if size==1:
            self.container['recursionHeapsPermutation'].append(''.join(word))

        for i in range(size):
            self.recursionHeapsPermutation(size-1, word=word)
            if size & 1:
                word[0], word[size-1] = word[size-1], word[0]
            else:
                word[i], word[size-1] = word[size-1], word[i]

    @__testTime
    def recursionBacktrackingPermutation(self, length: int, word: list, i: int=0):
        if i ==length:
            self.container['recursionBacktrackingPermutation'].append(''.join(word))
        else:
            for x in range(i, length):
                word[i], word[x] = word[x], word[i]
                self.recursionBacktrackingPermutation(length, word, i+1)
                word[i], word[x] = word[x], word[i]

    def __lexicographicPermutation(self, word: list):
        a = sorted(word)
        n = len(a) - 1
        while True:
            yield ''.join(a)

            #1. Find the largest index j such that a[j] < a[j + 1]
            for j in range(n-1, -1, -1):
                if a[j] < a[j + 1]:
                    break
            else:
                return

            #2. Find the largest index k greater than j such that a[j] < a[k]
            v = a[j]
            for k in range(n, j, -1):
                if v < a[k]:
                    break

            #3. Swap the value of a[j] with that of a[k].
            a[j], a[k] = a[k], a[j]

            #4. Reverse the tail of the sequence
            a[j+1:] = a[j+1:][::-1]

    @__testTime
    def lexicoGraphicPermutation(self, word: list):
        result = list(self.__lexicographicPermutation(word))
        for i in result:
            self.container['lexicoGraphicPermutation'].append(i)

Object=BestPermutationAlgorithm('poiuytr')


