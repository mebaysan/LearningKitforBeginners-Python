import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017")

myDb = myClient['python_nosql']

myCollection = myDb['products']

myCollection.update_one( # update_one bulduğu ilk kaydı günceller
    {'name': 'Iphone 7'},  # name'i Iphone 7 olanı seç
    {'$set':  # update operatoru
         {'name': 'Değişen İsim'}  # name'i Değişen isim ile değiştir
     }
)

myCollection.update_many( # bulduğu tüm kayıtları günceller
    {'name': 'Laptop'},  # name'i Laptop olanları seç
    {'$set':  # update operatoru
         {'name': 'Dell ( Değişen )'}  # name'i Dell ( Değişen ) ile değiştir
     }
)
