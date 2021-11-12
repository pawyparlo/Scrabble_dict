import sqlite3 as sq

class Database:
    def __init__(self):
        self.c = sq.connect('letters.db') # Create database

        try:
            self.__create_table()
        except:
            print(f'Table already created')

    def __create_table(self):
        cur = self.c.cursor()
        cur.execute('''CREATE TABLE letters(
                       letter TEXT)''')
        self.c.commit()

    def search(self, letter):
        cur = self.c.cursor()
        database_content = self.__collect_letters()

        if letter in database_content:
            return True
        else:
            return False

    def __collect_letters(self):
        cur = self.c.cursor()
        cur.execute('''SELECT letter FROM letters''')
        result = cur.fetchall()

        overwritted_content = []
        for row in result:
            overwritted_content.append(row[0])
        self.c.commit()

        return overwritted_content

    def show_content(self):
        cur = self.c.cursor()
        cur.execute('''SELECT letter FROM letters''')
        result = cur.fetchall()

        for row in result:
            print(f'Current letters {row[0]}')

        self.c.commit()
                
    def addcontent(self, letter):
        cur = self.c.cursor()
        letter_record = letter
        cur.execute(f'''INSERT INTO letters(letter)
                        VALUES(?)''', (letter_record))
        self.c.commit()

    def del_content(self, letter):
        cur = self.c.cursor()
        cur.execute('''DELETE FROM letters WHERE 
                          letter = ?''', (letter)).rowcount
        
        self.c.commit()


