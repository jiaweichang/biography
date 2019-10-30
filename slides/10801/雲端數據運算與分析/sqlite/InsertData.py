import sqlite3

conn = sqlite3.connect('user.db')
cursor = conn.cursor()
insert_query = 'INSERT INTO users VALUES(?, ?, ?, ?)'

users = []

users.append((None, 'Gary', 'gary@gmail.com', '123456'))
users.append((None, 'Jason', 'jason@gmail.com', '123456'))
users.append((None, 'Anita', 'anita@gmail.com', '123456'))

cursor.executemany(insert_query, users)

conn.commit()
conn.close()