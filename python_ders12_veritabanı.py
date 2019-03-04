import sqlite3

connection=sqlite3.connect("/root/Masaüstü/databaseexample/servis_kayıt.db")

cursor=connection.cursor()

cursor.execute(""" CREATE TABLE servis_kayıt(
kayıt_no INTEGER PRIMARY KEY,
ogrenci_no INTEGER NOT NULL,
adı VARCHAR(50),
soyadı VARCHAR(50),
ev_adresi VARCHAR(200)

)	""")

"""
import sqlite3     -> diyerek sqlite3 pythona dahil ediyoruz
connection = sqlite3.connect(/root/Masaüstü/deneme/öylesine.db")      -> connection değişkenine sqlite3.connect fonksiyonu ile bağlandık. () parantez içindeki dizine en son parametreye verdiğimiz isimde database oluştur dedik.(EĞER O İSİMDE YOKSA OLUŞTURUR,VARSA O DATABESE'İ AÇAR)
cursor=connection.cursor()       -> cursor isimli değişken ile connection değişkenindeki database'e bağlanıyoruz ve üzerinde ekleme çıkarma oynama yapabiliyoruz

cursor.execute( " CREATE TABLE deneme(
kayıt_no INTEGER PRIMARY KEY,	)")                -> cursor.execute ile cursor değişkenimizin bağlı olduğu database'e CREATE TABLE deneme diyerek deneme adında yeni bir tablo oluşturduk.

VERİ EKLEMEK:
INSERT INTO tablo_adı (alanlar) VALUES (değerler)

KALAN KISMI MUSTAFA BAŞER PYTHON KİTABINDA OLDUĞU İÇİN DAHA FAZLA YAZMAYACAĞIM

ÖNEMLİ NOT!: connection.close() değişkeni ile mutlaka bağlantıyı kesmeliyiz arkada bekleyen diğer işlemler kalmasın..

### VERİTABANINA ALDIĞIN İNPUTLARI EKLERKEN VALUES KISMINA (?,?,?) KOY KAÇ PARAMETRE VARSA ONDAN SONRA (input1,input2,imput3) diyerek aldığın inputlarıı ekle.


"""