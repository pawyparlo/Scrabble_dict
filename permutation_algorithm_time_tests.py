from itertools import permutations
from time import time


class BestPermutationAlgorithm():
    word = list('mauelyr')

    def __init__(self):
        self.container = []

        self.__testTime(self.itertoolsPermutations)
        self.__testTime(self.recursionPermutations)
        self.__testTime(self.recursionHeapsPermutation)
        self.__testTime(self.recursionBacktrackingPermutation)
        self.__testTime(self.lexicoGraphicPermutation)
    

    def itertoolsPermutations(self, word=word):
        perms = [''.join(x) for x in permutations(word)]
        return len(perms)

    def recursionPermutations(self, word=word ,step=0):
        try:
            if step==len(word):
                self.container.append(''.join(word))

            for i in range(step, len(word)):
                string_copy = word
                string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

                self.recursionPermutations(string_copy, step+1)
        except:
            pass

        finally:
            return len(self.container)

    def recursionHeapsPermutation(self, size=len(word), word=word):
        try:
            if size==1:
                self.container.append(''.join(word))

            for i in range(size):
                self.recursionHeapsPermutation(size-1, word=word)
                if size & 1:
                    word[0], word[size-1] = word[size-1], word[0]
                else:
                    word[i], word[size-1] = word[size-1], word[i]
        except:
            pass

        finally:
            return len(self.container)

    def recursionBacktrackingPermutation(self, word=word, i=0, length=7):
        try:
            if i ==length:
                self.container.append(''.join(word))
            else:
                for x in range(i, length):
                    word[i], word[x] = word[x], word[i]
                    self.recursionBacktrackingPermutation(word, i+1, length)
                    word[i], word[x] = word[x], word[i]
        except:
            pass

        finally:
            return len(self.container)     

    def __lexicographicPermutation(self, word: list=word):
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

    def lexicoGraphicPermutation(self, word=word):
        var = list(self.__lexicographicPermutation(word))
        return len(var)


    # Decorator
    def __testTime(self, func):
        start_time = time()
        len = func()
        end_time = time()
        print(f'Algorithm: {func.__name__} \n time: {(end_time-start_time):.8f} \n nr of permutations: {len}')
        self.container.clear()


Object=BestPermutationAlgorithm()


