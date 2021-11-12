from database import Database

class LetterContainer(Database):

    def __init__(self):
        super().__init__() # Create database

    def check_letters(self):
        self.show_content() #Database

    def collect_letters(self):
        count = int(input('How much letters you want to add (max 7): '))
        assert count <= 7, f"You can't add more than 7 letters"
        
        for i in range(1, count + 1, 1):    
            letter = str(input(('Input letter: ')))
            self.addcontent(letter)

            print(f'{letter} added')

    def remove_letter(self):
        count = int(input('How much letters you want to remove: '))
        assert count <= 7, f'Enter number in range (1-7)'

        for i in range(1, count+1, 1):
            letter = str(input(('Input letter which you want remove: ')))   
            letter_state = self.search(letter)

            if letter_state == True:
                self.del_content(letter)
                print(f'{letter} removed')
            elif letter_state == False:
                print(f"{letter} doesn't found in database")

            else:
                print("Letter doesn't exist") 


# Basic interface
user_choice = 10
Game  = LetterContainer()

# Start game = collect 7 letters 
while user_choice != 0:
    print('''Menu:
            1. Add letters: 
            2. Remove letters:
            3. Show letters''')

    if user_choice == 1:
        Game.collect_letters()

    elif user_choice == 2:
        Game.remove_letter()

    elif user_choice == 3:
        Game.check_letters()
    
    user_choice = int(input('Enter your choice: '))



