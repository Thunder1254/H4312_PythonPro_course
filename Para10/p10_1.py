import sqlite3

connection  = sqlite3.connect("ITStepDB.sl3", 5)
cur = connection.cursor()

# створення таблиці з  ім'ям (first_table) та одним полем
#cur.execute("CREATE TABLE first_table(name TEXT);")

#вставлення в таблицю first_table значення в поле name
#cur.execute("INSERT INTO first_table VALUES('LEONARDO')")
#cur.execute("INSERT INTO first_table VALUES('Lorraine')")
#cur.execute("INSERT INTO first_table VALUES('Eduard')")
connection.commit()

#отримуємо і друкуємо значення з таблиці
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
result = cur.fetchall()
print(result)

connection.close()