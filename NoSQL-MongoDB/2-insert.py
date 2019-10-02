import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017")

myDb = myClient['python_nosql']

myCollection = myDb['products']  # parametre olarak verdiğimiz collection'a bağlandı

# print(myDb.list_collection_names()) # veritabanındaki collection'ları listeler

# product = {"name": "Xiaomi redmi 5 plus", "price": 3000}
# result = myCollection.insert_one(product)
# print(result)
# print(type(result))
# print(result.inserted_id) # bize o ürünün eklenme id'sini gösterir

productList = [
    {"name": "Laptop", "price": 3000, "description": "Güzel Laptop"},
    {"name": "Telefon", "price": 2000, "categories": ["Iphone", "Samsung"]},
    {"isim": "Mouse", "price": 50},
    # istersek isim adında bir field oluşturabiliriz mongodb ortamında bir sorun teşkil etmez hata vermez fakat bizim için ileride sıkıntı olabilir
    {"isim": "Keyboard", "price": 120}
]
result = myCollection.insert_many(productList)  # çoklu eleman ekleyeceğimiz için many yaptık
print(result.inserted_ids)  # ekleyeceğimiz elemanların idsini görmek için ids yaptık
