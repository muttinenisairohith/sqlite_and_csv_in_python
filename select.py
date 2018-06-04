import sqlite3

conn = sqlite3.connect('sqlite.db')

print("opened db")

cursor = conn.execute("SELECT ID,NAME ,ANGLE,PRIORITY from SERVO")

for row in cursor:
    print ("ID=",row[0])
    print("name=",row[1])
    print("ANGLE=",row[2])
    print("PRIOROITY=",row[3])


print("operation done")

conn.close()
