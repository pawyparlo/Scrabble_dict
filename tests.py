from database import Database
from data_processing import DataContainer
from math import factorial


class DataProcessingTests(DataContainer):
    def __init__(self):
        super().__init__()
        self.objectname = DataContainer()
        self.__colectPermutations()

    def tryCreateobject(self):
        return self.objectname != None

    def tryCollectletters(self):
        return self.collectLetters() != None

    def __colectPermutations(self):
        self.objectname.listPermutation(self.collectLetters(),len(self.collectLetters()))
        self.permutations = self.objectname.permutation_list

    def tryTopermuteList(self):
        var = self.collectLetters()
        return len(self.permutations) == factorial(len(var))

    def tryPrintpermutations(self):
        for i in range(0, len(self.permutations), 3):
            try:
                print(self.permutations[i],
                      self.permutations[i+1],
                      self.permutations[i+2])
            except IndexError:
                pass

    def tryPrintletters(self):
        return self.collectLetters()

    def main_function(self):
        return self.listPop()

    def __repr__(self):
        return 


class DataBaseTests(Database):
    def __init__(self):
        super().__init__()
        self.objectname = Database

    def tryCreatetable(self):
        if self.objectname != None:
            return True
        else:
            return False
