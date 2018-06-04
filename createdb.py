import sqlite3

conn = sqlite3.connect('sqlite.db')

print("opened db")

conn.execute('''CREATE TABLE COMPANY
(ID PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')

print("table created")

conn.close()
