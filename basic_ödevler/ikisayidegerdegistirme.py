#Kullanıcıdan iki adet sayı alıp bu sayıların değerlerini değiştireceğiz.

a = input("a:")
b = input("b:")

print("Değiştirilmeden Önce Değerler\na: {} b: {}\n".format(a,b))

a,b = b,a

print("Değiştirildikten Sonraki Değerler\na: {} b: {}\n".format(a,b))
