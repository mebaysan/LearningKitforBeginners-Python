import pymongo
from bson.objectid import ObjectId  # mongodb tarafında _id'ye göre find yapmak için gerekli

myClient = pymongo.MongoClient("mongodb://localhost:27017")

myDb = myClient['python_nosql']

myCollection = myDb['products']

# filter = {"name": "Laptop"}
# result = myCollection.find(filter)  # filtreleme yaptık ve name alanı Laptop olanları getirdik sadece
# for i in result:
#     print(i)


# result = myCollection.find_one({"_id": ObjectId("5d94f5d7671b5c3a552e47bf")}) # bize ilgili object id'ye sahip olan kaydı döner
# # id'ye göre arama yaparken id'ler ObjectId formatına dönüştürülmelidir.
# print(result)

result = myCollection.find({
    "name": {
        "$in": ["Laptop", "Telefon", "Olmayan Deger"]
        # name alanında bu değerler varsa dönecek, böyle bir filtreleme yaptık
    }
})
result2 = myCollection.find({
    "price": {
        "$gt": 2000  # greater than -> price field'ı 2000'den büyük olanları alır
    }
})
result3 = myCollection.find({
    "price": {
        "$gte": 3000  # greater than equal -> price field'ı 3000'den büyük veya eşit olanları alır
    }
})
result3 = myCollection.find({
    "price": {
        "$eq": 3000  # equal -> price field'ı 3000'e eşit olanları alır
    }
})
result4 = myCollection.find({
    "price": {
        "$lt": 3000  # less than -> price field'ı 3000'den küçük olanları alır
    }
})
result5 = myCollection.find({
    "price": {
        "$lte": 3000  # less than equal -> price field'ı 3000'den küçük veya eşit olanları alır
    }
})
# mongodb operators sitesinden bu operatörlere bakabiliriz

result6 = myCollection.find({
    "name": {"$regex": "^I"} # regex yazarak filtreleme yapabiliriz -> name field'ı I ile başlayanları getir dedik
})
for i in result6:
    print(i)
