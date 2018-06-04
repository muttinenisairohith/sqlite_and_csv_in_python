import sqlite3

conn = sqlite3.connect('sqlite.db')

print("opened db")

conn.execute('''CREATE TABLE alpha
(ID PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
ANGLE INT NOT NULL,
PRIORITY INT NOT NULL);''')

print("table created")

conn.close()
