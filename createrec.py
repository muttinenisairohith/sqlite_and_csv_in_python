import sqlite3

conn = sqlite3.connect('sqlite.db')

print("opened db")

conn.execute("INSERT INTO COMPANY (ID,NAME ,AGE,ADDRESS,SALARY)\
VALUES(1,'PAUL',32,'INDIA',50000)")

conn.commit()

print("records created")

conn.close()
