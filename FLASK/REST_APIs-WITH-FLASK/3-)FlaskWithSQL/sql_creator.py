import sqlite3

conn = sqlite3.connect('data.db')

cursor = conn.cursor()

# create_table_query = "create table users (id int, username text, password text)"
# cursor.execute(create_table_query)

add_user_query = "insert into users values (?, ?, ?)"


User = (1, 'baysan', 'asd')
# tuple olarak ? ? ? lara karşılık gelen değeri veriyoruz
cursor.execute(add_user_query, User)


USERS = [
    (2, 'baysan2', 'asd'),
    (3, 'baysan3', 'asd'),
    (4, 'baysan4', 'asd'),
    (5, 'baysan5', 'asd'),
]

cursor.executemany(add_user_query, USERS)  # çoklu query çalıştırmamızı sağlar

conn.commit()  # bağlantı üzerinde yaptığımız değişiklikleri onaylıyoruz

conn.close()  # bağlantıyı kapatıyoruz
