import sqlite3 as sq


class Database:
    def __init__(self):
        self.c = sq.connect('letters.db') # Create database
        try:
            self.__createTable()

        except:
            print(f'Table already created')

    def __createTable(self):
        cur = self.c.cursor()
        cur.execute('''CREATE TABLE letters(
                       letter TEXT)''')
        self.c.commit()

    def search(self, letter):
        database_content = self.collectLetters()
        return letter in database_content

    def collectLetters(self):
        cur = self.c.cursor()
        cur.execute('''SELECT letter FROM letters''')
        result = cur.fetchall()
        self.c.commit()
        return [row[0] for row in result]

    def showContent(self):
        cur = self.c.cursor()
        cur.execute('''SELECT letter FROM letters''')
        result = cur.fetchall()

        for row in result:
            print(f'Current letters {row[0]}')

        self.c.commit()
                
    def addContent(self, letter):
        cur = self.c.cursor()
        letter_record = letter
        cur.execute(f'''INSERT INTO letters(letter)
                        VALUES(?)''', (letter_record))
        self.c.commit()

    def deleteContent(self, letter):
        cur = self.c.cursor()
        cur.execute('''DELETE FROM letters WHERE 
                          letter = ?''', (letter))
        self.c.commit()

