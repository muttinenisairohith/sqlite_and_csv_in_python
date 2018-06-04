import sqlite3

conn = sqlite3.connect('sqlite.db')

print("opened db")

conn.execute("INSERT INTO SERVO (ID,NAME ,ANGLE,PRIORITY)\
VALUES(2,'ELBOW',95,5)")

conn.commit()

print("records created")

conn.close()
