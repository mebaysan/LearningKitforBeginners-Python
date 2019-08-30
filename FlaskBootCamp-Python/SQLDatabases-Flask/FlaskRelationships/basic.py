# Create Entries Into The Tables!

from models import db, Ponny, Owner, Toy
# 2 Ponny oluştur
rufus = Ponny("Rufus")
fido = Ponny('Fido')
# Ponnyleri dbye kaydet
db.session.add_all([rufus, fido])
db.session.commit()
# Kontrol objects
print(Ponny.query.all())

# adı Rufus olan objelerden ilkini seçer.  .all() deseydik liste dönerdi
rufus = Ponny.query.filter_by(name='Rufus').first()
print(rufus)
# Create Owner
jose = Owner('Jose', rufus.id)

# Give Rufus some toys
toy1 = Toy('Toy1', rufus.id)
toy2 = Toy('Toy2', rufus.id)
toy3 = Toy('Toy3', rufus.id)

# oluşturduğumuz nesnelerin hepsini veritabanına ekledik
db.session.add_all([jose, toy1, toy2, toy3])
db.session.commit()  # kayıt yaptık

# Rufus'u yakala değişiklikleri gör!
rufus = Ponny.query.filter_by(name='Rufus').first()
print(rufus)

print("**********")
rufus.report_toys()