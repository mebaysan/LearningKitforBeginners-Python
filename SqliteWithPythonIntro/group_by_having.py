import sqlite3

conn = sqlite3.connect("database/chinook.db")

cursor = conn.cursor()

cursor.execute(" select city,count(*) from customers group by city having count(*)>0 order by count(*) desc ") # -> Hangi şehirde kaç customer var sorgusu. city ve count seç(bütün count-adedi) seç customers tablosundan ve grupla city'e göre ve city'e göre büyükten küçüğe sırala
                                                                    # having count(*)>0 -> sayısı 0'dan büyük olanları bana getir
for data in cursor:
    print("Şehir adı = {}\nBağlı Customer Adedi = {}\n**********".format(data[0],data[1]))


conn.close()