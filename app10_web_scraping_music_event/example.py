import sqlite3

connection = sqlite3.connect("mydata.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()

print(rows)

cursor.execute()