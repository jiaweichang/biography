import sqlite3

conn = sqlite3.connect('log.db')

cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS logs')
cursor.execute('CREATE TABLE IF NOT EXISTS logs('
               'id INTEGER PRIMARY KEY, '
               'name TEXT, '
               'message TEXT)')

conn.commit()
conn.close()