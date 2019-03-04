print("""
****************
Kullanıcı Girişi Programı v1.1
#Bu programda id: baysan password: 12345

****************
""")
kullanici_id="baysan"
kullanici_pass="12345"
giriş_hakki=3

while True:
    kullanici_id_gir=input("Kullanıcı Adı: ")
    kullanici_pass_gir=input("Şifre: ")
    if(kullanici_id_gir != kullanici_id and kullanici_pass_gir== kullanici_pass):
        print("Kullanıcı Adı Hatalı...")
        giriş_hakki-=1
    elif(kullanici_id_gir == kullanici_id and kullanici_pass_gir!= kullanici_pass):
        print("Parola Hatalı...")
        giriş_hakki-=1
    elif(kullanici_id_gir!= kullanici_id and kullanici_pass_gir!= kullanici_pass):
        print("Kullanıcı Adı ve Parola Hatalı...")
        giriş_hakki-=1
    else:
        print("Sisteme Başarılı Bir Şekilde Girildi...")
        break
    if(giriş_hakki == 0):
        print("Giriş Hakkınız Bitti...")
        break
        
    
