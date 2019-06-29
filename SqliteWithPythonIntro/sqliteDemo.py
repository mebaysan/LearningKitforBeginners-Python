import sqlite3 # sqlite3 modülünü dahil ettik

conn = sqlite3.connect("database/chinook.db") # veri tabanına bağlanıyoruz. Aynı dizinde olduğu için direk db adı yazdık

cursor = conn.cursor() # veritabanına erişmek için bir nesne oluşturduk

cursor.execute("Select * from customers where city = 'Prague' ") # execute diyerek sorgu çalıştırıyoruz ve sorgudan gelen data cursor içine geldi

for data in cursor: # cursor içindehi herbir data için dedik
    print("First Name = {}'s Id = {} and Last Name = {}".format(data[1],data[0],data[2])) # gelen data'nın ikinci elemanı aldık