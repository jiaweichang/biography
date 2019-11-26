import sqlite3

conn = sqlite3.connect('log.db')
cursor = conn.cursor()

for row in cursor.execute('SELECT * FROM logs'):
    print(row)

conn.commit()
conn.close()