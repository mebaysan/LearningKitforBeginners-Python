print("""*************************
ATM Makinesine Hoşgeldiniz.
işlemler;
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan çıkmak için "q" tuşlayın.
*********************""")

bakiye=1000

while True:
    işlem=input("İşlem Girin:")

    if(işlem=="q"):
        print("Yine Bekleriz...")
        break
    elif(işlem=="1"):
        print("Bakiye : {} tl dir".format(bakiye))

    elif(işlem=="2"):
        miktar=int(input("miktar girin"))
        print("Yeni bakiye : {}".format(bakiye+miktar))

        bakiye+=miktar

    elif(işlem=="3"):
        miktar=int(input("miktar girin"))
        if(bakiye-miktar<0):
            print("Bakiye yetersiz")
            continue
        bakiye-=miktar

    else:
        print("Geçersiz İşlem....")
    
