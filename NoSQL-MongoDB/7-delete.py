import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017")

myDb = myClient['python_nosql']

myCollection = myDb['products']

myCollection.delete_one({'name': 'Xiaomi redmi 5 plus'}) # name field'ı Xiaomi redmi 5 plus olan kaydı siler (ilk bulduğunu)

result = myCollection.delete_many({'name': 'Telefon'}) # name field'ı Telefon olan tüm kayıtları siler


print(f"{result.deleted_count} kayıt silindi") # bize silinen kayıt sayısını verir