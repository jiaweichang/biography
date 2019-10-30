import sqlite3

conn = sqlite3.connect('user.db')

cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('CREATE TABLE IF NOT EXISTS users('
               'id INTEGER PRIMARY KEY, '
               'name TEXT, '
               'email TEXT, '
               'password TEXT)')

conn.commit()
conn.close()