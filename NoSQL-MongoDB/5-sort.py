import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017")

myDb = myClient['python_nosql']

myCollection = myDb['products']

result = myCollection.find().sort("price",-1) # büyükten küçüğe sıralama yapar fakat 1 verirsek küçükten büyüğe sıralama yapar
result2 = myCollection.find().sort([('name',1),('price',-1)]) # name field'a göre küçükten büyüğe yaparken price field'a göre büyükten küçüğe yapar
for i in result2:
    print(i)