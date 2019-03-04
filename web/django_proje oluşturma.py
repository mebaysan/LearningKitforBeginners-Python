print("""
pip install django
pip3 install django
pip3 install virtualenv
pip install virtualenv
Gerekli ortamları kurduk (django kütüphanesi ve virtualenv python sanal ortamı)

projemizi oluşturacağımız dizine geliyoruz:
1-) virtualenv sanalortam_adı                 -> oluşturacağımız sanal ortamın adını parametre olarak girip sanal ortam oluşturuyoruz
2-) source sanalortam_adı/bin/activate        -> oluşturduğumuz sanal ortamı aktif hale getiriyoruz
3-) django-admin startproject proje_adı .     -> projemizi oluşturuyoruz. '.' koymamızın sebebi sanal ortamla aynı dizinde kurulmasını söyledik gereksiz dosya oluşturmasın
4-) python manage.py runserver                -> serveri çalıştırdık. başarılı olursak zaten bize localhost verecek ordan sunucuya giriş yapabiliriz.
5-) deactivate                                -> aktif ettiğimiz sanal ortamdan çıkmak için uçbirime direk deactivate yazmamız yeterlidir.














	""")