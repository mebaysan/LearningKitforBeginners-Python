print("""
					İleri Seviye Karakter Dizileri (Stringler)


upper() ve lower()

upper() metodu stringin tüm karakterlerini büyük harfe çevirir.

lower() metodu stringin tüm karakterlerini küçük harfe çevirir.

ÖRNEK:
"baysan".upper()
"BAYSAN".lower()
ÇIKTISI:
	""")
print("baysan".upper())
print("BAYSAN".lower())
print("""***************************************************


replace()
replace(x,y) : Stringteki x değerlerini y ile değiştirir.
ÖRNEK:
"Herkese anana babana bana selam söyle gardaş".replace("a","o")
"BAYSAN".replace("bay","bayan")
ÇIKTISI:
	""")
print("Herkese anana babana bana selam söyle gardaş".replace("a","o"))
print("BAYSAN".replace("bay","bayan"))
print("""******************************

startswith() ve endswith()

startswith(x) : String x ile başlıyorsa True, başlamıyorsa False değeri döndürür.

endswith(x) : String x ile bitiyorsa True, bitmiyorsa False değeri döndürür.
ÖRNEKLER:
"Baysan".startswith("bay")
"Baysan".endswith("sam")
ÇIKTISI:
	""")
print("Baysan".startswith("bay"))
print("Baysan".endswith("sam"))
print("""**************************************************
split()
split(a) : Verilen bir a değerine göre string parçalara ayrılarak herbir parça listeye atılır.
ÖRNEKLER:
liste = "Python Programlama Dili".split(" ") # Boşluk karakterine göre ayrıldı.
liste2 = "Python-Php-Java-C-Javascript".split("-")
ÇIKTISI:
	""")
liste = "Python Programlama Dili".split(" ")
print(liste)
liste2 = "Python-Php-Java-C-Javascript".split("-")
print(liste2)
print("""**************************************************
join()
Listenin elemanlarını bir string değeriyle birleştirmemizi sağlar.
liste = ["21","02","2014"]
"/".join(liste)
ÇIKTISI:
	""")
liste = ["21","02","2014"]
print("/".join(liste))
print("""*************************************
count()
count(x): Stringin içindeki x değerlerini sayar.
count(x,index): Stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar.
ÖRNEK:
"ada kapısı yandan çarklı".count("a",2)
ÇIKTISI:
	""")
print("ada kapısı yandan çarklı".count("a",2))
print("""
find() ve rfind()
find(x) : x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.
rfind(x) : x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.
ÖRNEKLER:
"araba".find("a")
"araba".rfind("s")
ÇIKTISI:
	""")
print("araba".find("a"))
print("araba".rfind("s"))