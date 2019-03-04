import random
import time

class Canavar():
	def __init__(self,can=150,zırh=75,hasar=random.randint(10,25)):
		self.can=can
		self.zırh=zırh
		self.hasar=hasar


class Oyuncu():
	def __init__(self,can=100,zırh=60,hasar=12):
		self.can=can
		self.zırh=zırh
		self.hasar=hasar



print("""
				KodxMons Savaş Oyununa Hoş Geldin...
Hasar Vermek İçin -> '1'
Can Yenilemek İçin -> '2'   """)
oyuncu=Oyuncu()
KodxMons=Canavar()
while True:
	işlem=input("Hareket Belirle : ")
	if(işlem=="1"):
		KodxMons.can-=oyuncu.hasar
		print("Hasar verildi KodxMons'un kalan canı : ",KodxMons.can)
		time.sleep(1)
		print("KodxMons Bizim için bir işlem yapacak")
		rasgeleişlem=random.randint(1,2)
		if(rasgeleişlem==1):
			KodxMons.can+=8
			print("OLAMAZ! KodxMons Can Yeniledi, Yeni canı :",KodxMons.can)
		elif(rasgeleişlem==2):
			oyuncu.can-=KodxMons.hasar
			print("Offff! KodxMons Bize Hasar Verdi, Kalan Canımız : ",oyuncu.can)
	elif(işlem=="2"):
		oyuncu.can+=8
		print("Biraz Bekle Can Yenileniyor...")
		time.sleep(1)
		print("Harika can Yenilendi Yeni can : ",oyuncu.can)
		print("KodxMons Bir İşlem Yapacak")
		time.sleep(1)
		rasgeleişlem=random.randint(1,2)
		if(rasgeleişlem==1):
			KodxMons.can+=8
			print("OLAMAZ! KodxMons Can Yeniledi, Yeni canı :",KodxMons.can)
		elif(rasgeleişlem==2):
			oyuncu.can-=KodxMons.hasar
			print("Offff! KodxMons Bize Hasar Verdi, Kalan Canımız : ",oyuncu.can)
	if(oyuncu.can<=0):
		print("GAME OVER!!!")
		break