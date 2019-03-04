import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from datetime import *
print("""
*****************************************
Database'den mail adresi çekip, öğrenci okula gelmedi maili atma (deneme) projesine hoşgeldiniz...
*****************************************
İşlemler;
1-)Öğrenci Eklemek
2-)Öğrenci Velisine Yoklama Maili Atmak
3-)Kayıtlı Öğrencileri Görmek İçin

#Çıkmak için 'x' basın... 
""")
while True:
	işlem=input("İşlem Seçiniz : ")
	if(işlem=="1"):
		öğrenci_no=int(input("Öğrenci Numarasını Girin : "))
		adı=input("Öğrenci Adını Girin : ")
		soyadı=input("Öğrenci Soyadını Girin : ")
		veli_mail=input("Veli Mail Adresini Girin : ")
		connection=sqlite3.connect("/root/Masaüstü/python-ders/veritabanı_mail_proje/yoklama.db")
		cursor=connection.cursor()
		cursor.execute(""" INSERT INTO öğrenci_bilgileri(öğrenci_no,adı,soyadı,veli_mail) VALUES (?,?,?,?)""",(öğrenci_no,adı,soyadı,veli_mail))
		print("Öğrenci Bilgileri Kaydediliyor...")
		print("Öğrenci Bilgileri Kaydedildi...")
		connection.close()
	elif(işlem=="2"):
		şu_an=datetime.now()
		öğrenci_no=int(input("Velisine Mail Göndermek İstediğiniz Öğrencinin Okul Numarasını Girin : "))
		connection=sqlite3.connect("/root/Masaüstü/python-ders/veritabanı_mail_proje/yoklama.db")
		cursor=connection.cursor()
		cursor.execute(" SELECT veli_mail FROM öğrenci_bilgileri Where öğrenci_no = ? ",(öğrenci_no,)) # input olarak alınan öğrenci_no 'nun çekilmesini istiyoruz burada.
		mail_adresi=cursor.fetchall()
		gönderilecek_mail=mail_adresi[0]
		print("Bilgilendirme mesajı gönderilecek mail adresi : ", gönderilecek_mail[0])
		mesaj=MIMEMultipart()
		mesaj["From"]="info.baysansoftwear@gmail.com"
		mesaj["To"]= gönderilecek_mail[0]
		mesaj["Subject"]="Veli Yoklama Bilgilendirme Sistemi"
		yazı="Velisi bulunduğunuz {} numaralı öğrenci {} tarihinde  okula gelmemiştir.".format(öğrenci_no,datetime.strftime(şu_an,"%D"))
		mesaj_gövdesi=MIMEText(yazı,"plain")
		mesaj.attach(mesaj_gövdesi)
		try:
			mail=smtplib.SMTP("smtp.gmail.com",587)
			mail.ehlo()
			mail.starttls()
			mail.login("info.baysansoftwear@gmail.com","deneme_şif")
			mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
			print("Mail Başarıyla Gönderildi...")
			mail.close()
		except:
			sys.stderr.write("Mail Gönderimi Başarısız Oldu...\n")
			sys.stderr.flush()
		connection.close()
	elif(işlem=="x"):
		print("Programdan Çıkılıyor...\nEğitim Önemli,Çocuklarımız Okuldan Kaçmasın...")
		break
	elif(işlem=="3"):
		connection=sqlite3.connect("/root/Masaüstü/python-ders/veritabanı_mail_proje/yoklama.db")
		cursor=connection.cursor()
		cursor.execute("SELECT * FROM öğrenci_bilgileri ")
		liste=cursor.fetchall()
		print("Öğrenci Bilgileri Geliyor....")
		for i in liste:
			print(i)
	else:
		print("Geçersiz İşlem...")
