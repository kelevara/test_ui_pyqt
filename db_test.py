import sqlite3

connect = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = connect.cursor()

cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
result = cursor.fetchall()

print(result)

connect.close()
