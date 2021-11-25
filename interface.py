from data_processing import DataContainer
from database import Database
from data_processing import DataContainer
import sys

class LetterContainer(DataContainer):

    def __init__(self):
        super().__init__() # Create database

    def checkLetters(self):
        print(self.collectLetters())

    def newLetters(self):
        count_add = int(input('How much letters you want to add (max 7): '))
        assert count_add <= 7, f"You can't add more than 7 letters"
        for _ in range(1, count_add + 1, 1):    
            letter = str(input(('Input letter: ')))
            self.addContent(letter)

            print(f'{letter} added')

    def removeLetters(self):
        count_del = int(input('How much letters you want to remove: '))
        assert count_del <= 7, f'Enter number in range (1-7)'

        for i in range(1, count_del + 1, 1):
            letter = str(input(('Input letter which you want remove: ')))   
            letter_state = self.search(letter)

            if letter_state == True:
                self.deleteContent(letter)
                print(f'{letter} removed')

            elif letter_state == False:
                print(f"{letter} doesn't found in database")

            else:
                print("Letter doesn't exist") 

    def findWords(self):
        return self.listPop()

        


# Basic interface
user_choice = 10
Game  = LetterContainer()

# Start game = collect 7 letters 
while True:

    print('''Menu:
            1. Add letters: 
            2. Remove letters:
            3. Show letters
            4. Find matching words
            5. Exit''')


    user_choice = int(input('Enter your choice: '))

    while user_choice != 0:
        
        if user_choice == 1:
            Game.newLetters()
            break

        elif user_choice == 2:
            Game.removeLetters()
            break

        elif user_choice == 3:
            Game.checkLetters()
            break

        elif user_choice == 4:
            Game.listPop()
            break

        elif user_choice == 5:
            sys.exit(0)


