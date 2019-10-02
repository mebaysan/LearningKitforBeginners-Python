import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017")

myDb = myClient['python_nosql']

myCollection = myDb['products']

# result = myCollection.find_one() # bulduğu ilk kaydı getirir
# print(result)

# for i in myCollection.find(): # bütün kayıtları getirir
#     print(i)

for i in myCollection.find({}, {'_id': 0, 'name': 1, 'price': 1}): # bütün kayıtların sadece field'ını 1 verdiklerimizi getirir. Görmek istemediklerimiz için 0 verebiliriz
    print(i)
