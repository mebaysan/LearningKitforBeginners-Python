import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

create_table_query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table_query)


create_table_query = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table_query)


conn.commit()

conn.close()
