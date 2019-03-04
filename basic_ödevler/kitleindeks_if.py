print("""Kitle indeks programı v1.1 coder by baysan
**************************************** 
BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
****************************************
 """)
boy=float(input("Boyunuzu Girin:"))

kilo=float(input("Kilonuzu Girin:"))

bki=kilo/boy*boy
if (bki<18.5):
	print(bki,"Zayıfsın.Kilo almaya bak.")
	pass
elif(bki<=25):
	print(bki,"Normalsin.Formunu koru.")
elif(bki<=30):
	print(bki,"Fazla kilolusun.Kilo vermeye çalış.")
elif(bki>30):
	print(bki,"Obez olmuşsun Dünyayı mı yiyecen şerefsiz....")
else:
	print(bki,"İnsan mısın ulan sen?")