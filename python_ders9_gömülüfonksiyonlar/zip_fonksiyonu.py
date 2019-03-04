print("""
Zip Fonksiyonu
zip fonksiyonu listelerin elemanları sırasıyla demet şeklinde gruplayarak bir tane liste oluşturuyor. 
liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10]

print(list(zip(liste1,liste2)))

ÇIKTISI:
	""")
liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11,12]

print(list(zip(liste1,liste2)))

print("""
Ufuk açıcı başka bir örnek yapalım...

     ## Aynı anda iki liste üzerinde gezinmek
liste4 = [1,2,3,4]
liste5 = ["Python","Php","Java","Javascript"]

for i,j in zip(liste4,liste5):
    print("i:",i,"j:",j)

ÇIKTISI:
	""")
## Aynı anda iki liste üzerinde gezinmek
liste4 = [1,2,3,4]
liste5 = ["Python","Php","Java","Javascript"]

for i,j in zip(liste4,liste5):
    print("i:",i,"j:",j)
    