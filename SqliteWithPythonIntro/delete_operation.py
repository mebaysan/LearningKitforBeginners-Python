import sqlite3

conn = sqlite3.connect("database/chinook.db")

cursor = conn.cursor() # bağlantı oluşturduk
sorgu = " delete from customers where customerid=60 " # customers'dan sil customerid'si 60 olanlari
cursor.execute(sorgu) # sorguyu çalıştırdık
conn.commit() # veritabanında değişiklik yaptığımız için commit ettik
conn.close() # bağlantıyı kapattık