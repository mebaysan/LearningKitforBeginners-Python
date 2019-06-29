import sqlite3

conn = sqlite3.connect("database/chinook.db")

cursor = conn.cursor() # bağlantı oluşturduk
sorgu = " update customers set city='Umraniye' where city='Uskudar' " # customers güncelle, city'i Umraniye olarak guncelle ama city'si Uskudar olanlari
cursor.execute(sorgu) # sorguyu çalıştırdık
conn.commit() # veritabanında değişiklik yaptığımız için commit ettik
conn.close() # bağlantıyı kapattık