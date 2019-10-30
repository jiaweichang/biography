import sqlite3

conn = sqlite3.connect('user.db')
cursor = conn.cursor()

for row in cursor.execute('SELECT * FROM users'):
    print(row)

conn.commit()
conn.close()