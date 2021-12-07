from data_storage import DataContainer


class DataAlgorithms(DataContainer):
    def __init__(self):
        super().__init__()


    def searchIntoHashMap(self):

        if len(self.collectLetters()) < 3:
            self.permutationsToList(self.collectLetters(), len(self.collectLetters()))

            for permutations in self.permutation_list:

                for words in self.hashLetters[permutations[0]]:
                    if permutations == words:
                        print(words)

        elif len(self.collectLetters()) >= 3:      

            while len(self.collectLetters) != 0:
                self.permutationsToList(letters, len(letters))

                for permutations in self.permutation_list:

                    for words in self.hashLetters[permutations[0]]:
                        if permutations == words:
                            print(words)

                letters.pop()
                self.permutation_list.clear()   
                letters = self.removeLetter(letters)  

    def searchIntoSet(self):
        self.permutationsToSet(self.collectLetters(), len(self.collectLetters()))
        self.setData()

        print(self.permutation_set)
        # print(self.setLetters.intersection(self.permutation_set))


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

object = DataAlgorithms()
object.permutationsToSet(list('aou'),len(list('aou')))
object.setData()
print(object.permutation_set)
# print(object.permutation_set.intersection(object.setLetters))

object1 = DataAlgorithms()
object1.permutationsToList(list('aou'),len(list('aou')))
object.hashMapData()
print(object.permutation_list)



