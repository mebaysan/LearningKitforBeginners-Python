"""
Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur
1,1,2,3,5,8,13,21,34.......
"""
a=1
b=1

fibonacci=[a,b]    # -> fibonacci kuralı gereği 2 değerden oluşan bir liste oluşturduk

for i in range(10):
    a,b = b,a+b     # -> bu metodu 1. ders dosyasında görmüştük a'nın değerine b'nin değerini,b'nin değerine de a+b'nin değerini atıyoruz
    print("a:",a,"b:",b)

    fibonacci.append(b) #-> yeni b değerini oluşturduğumuz listemize atıyoruz
print(fibonacci)
