# Coder: Will Hoback
# Listener: Junyi Guo
# Sharer: Matheus Fernandes

import sqlite3

with open('candidates.txt', 'r') as input_file:
    reader = input_file.readlines()[1:]
    data = [row.strip().split("|") for row in reader]

db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS candidates")

cursor.execute('''CREATE TABLE candidates (
               id TEXT PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_init TEXT, 
               party TEXT NOT NULL)''')

db.commit() # Commit changes to the database

for item in data:
    cursor.execute('''INSERT INTO candidates (id, first_name, last_name, middle_init, party) VALUES (?,?,?,?,?)''', item)
    db.commit()


db.close()