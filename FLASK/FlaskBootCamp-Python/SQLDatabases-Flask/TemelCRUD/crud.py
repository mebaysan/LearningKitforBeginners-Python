from app import db, Person

## CREATE ##
insan = Person('Baysan', 20)  # instance oluşturduk
db.session.add(insan)  # oluşturudğumuz instance'i ekledik
db.session.commit()  # işlemi kayıt ettik

## READ ##
all_persons = Person.query.all()  # liste olarak bütün person objelerini döner
print(all_persons)

## SELECT BY ID ##
kisi_one = Person.query.get(1)  # id'si TemelCRUD olan objeyi getir dedik
print(kisi_one.name)  # gelen objenin adını ekrana bastırıyoruz

## FILTERS ##
kisi_filtering = Person.query.filter_by(
    name='Enes')  # name -> aramak istediğimiz kolon adı. name kolonu Enes olan objeyi getirir
print(kisi_filtering.all())  # name'i Enes olan bütün objeleri döner
# [*Enes 19 years old*]

## UPDATE ##
kisi_update = Person.query.get(1)  # id'si TemelCRUD olan objeyi seçtik
kisi_update.name = "Guncellenen Name"  # yakaladığımız objenin name'ini güncelledik
db.session.add(kisi_update)  # güncellenen objeyi veritabanına attık
db.session.commit()  # yaptığımız değişikliği kaydettik

## DELETE ##
kisi_delete = Person.query.get(2) # id'si 2 olan objeyi yakaladık
db.session.delete(kisi_delete) # yakaladığımız objeyi sildik
db.session.commit() # yaptığımız değişikliği güncelledik


butun_kisiler = Person.query.all()
print(butun_kisiler)