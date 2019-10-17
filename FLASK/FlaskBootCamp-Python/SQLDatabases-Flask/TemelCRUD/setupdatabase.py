from app import db, Person

db.create_all()  # Bütün tabloları oluşturur. Model ---> Db Table

kisi = Person('Enes', 19)  # instance oluşturduk
kisi2 = Person('Yusuf', 18)

print(kisi.id)  # burada none gelir çünkü daha kayıt yapmadık
print(kisi2.id)

db.session.add_all([kisi, kisi2])  # bu şekilde toplu liste halinde ekelyebiliriz
# db.session.add(kisi) # böyle tek tek de ekleyebiliriz
# db.session.add(kisi2)
db.session.commit()  # veritabanında değişiklik olduğu için kaydı gerçekleştiriyoruz
print(kisi.id)
print(kisi2.id)
