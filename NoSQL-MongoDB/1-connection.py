# pip install pymongo
import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017") # server'a bağlandı

myDb = myClient['python_nosql'] # veritabanına bağlanır ve parametre olarak aldığı veritabanı'na bağlanır yoksa oluşturur

print(myClient.list_database_names()) # Serverdaki collection'ları listeler
