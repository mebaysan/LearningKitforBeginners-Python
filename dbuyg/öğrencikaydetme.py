import sqlite3

print("""
DATABASE ÖĞRENCİ KAYDETME PROGRAMINA HOŞGELDİNİZ...  """)

öğrenci_no=int(input("Öğrenci Numaranızı Girin : "))
ad=input("Adınızı Girin : ")
soyad=input("Soyadınızı Girin : ")

connection=sqlite3.connect("/root/Masaüstü/python ders/dbuyg/bilgiler.db")
cursor=connection.cursor()

cursor.execute("""INSERT INTO bilgiler (öğrencinumarası,öğrenciadı,öğrencisoyadı) VALUES (?,?,?)""",(öğrenci_no,ad,soyad))