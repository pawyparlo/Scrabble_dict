from data_storage import DataContainer

from time import time


class DataAlgorithms(DataContainer):

    letters=list('krowat')

    def __init__(self):
        super().__init__()

        self.__testTime(self.returnFromHashMap)
        self.__testTime(self.searchIntoSet)


    def searchIntoHashMap(self, letters=letters):
        self.hashMapData() # Store data from .txt file into Hash Map
        self.itertoolsPermutations(letters) # Permute letters

        for permutations in self.permutation_list:
            for words in self.hashLetters[permutations[0]]:
                if permutations == words:
                    yield words

    def returnFromHashMap(self):
        result = list(self.searchIntoHashMap())
        return result

    def searchIntoSet(self, letters=letters):

        self.itertoolsPermutations(letters) # Permute letters
        self.setData() # Store .txt data into set
        result = self.setLetters.intersection(self.permutation_set)
        
        if len(result) > 0:
            return result


    # Decorator
    def __testTime(self, func):
        start_time = time()
        print(func())
        end_time = time()
        print(f'Algorithm: {func.__name__} \n time: {(end_time-start_time):.8f}')



Object=DataAlgorithms()




