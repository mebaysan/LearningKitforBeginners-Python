import sqlite3

def InsertDataForCustomers(ad,soyad,sehir,email):
    conn = sqlite3.connect("database/chinook.db")

    cursor = conn.cursor() # bağlantı oluşturduk
    sorgu = " insert into customers (firstName,lastName,city,email) values('{}', '{}', '{}', '{}')".format(ad,soyad,sehir,email) # sorgumuzu hazırladık
    cursor.execute(sorgu) # sorguyu çalıştırdık
    conn.commit() # veritabanında değişiklik yaptığımız için commit ettik
    conn.close() # bağlantıyı kapattık

InsertDataForCustomers('enes','baysan','Uskudar','deneme@gmail.com') # oluşturduğumuz fonksiyonu çalıştırdık