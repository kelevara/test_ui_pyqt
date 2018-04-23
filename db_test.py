import sqlite3
import pyodbc

connect1 = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = connect1.cursor()

con = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ=new_BD.mdb')
cur = con.cursor()

cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
result = cursor.fetchall()

cur.execute('SELECT [Год рождения] FROM [Общие данные]')
rez = cur.fetchall()

print(result)
print(rez)

connect1.close()
