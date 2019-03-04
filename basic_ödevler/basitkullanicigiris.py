print("""**************************
Kullanıcı Girişi
**************************
""")

print("Burada kullanıcıadını ve parolayı sistemde kayıtlıymış gibi düşünüyoruz\nvarsayılan id: baysan\nvarsayılan parola: 12345")
print("Denemek için kullanıcı adını,parolayı,ya da her ikisinide yanlış deneyebilirsiniz koşullu durumlar için basti bir örnektir.")
sys_kullanıcı_adı="baysan"
sys_parola="12345"

kullanıcı_adı=input("Kullanıcı Adı:")
parola=input("Parola:")

if (kullanıcı_adı==sys_kullanıcı_adı and sys_parola!=parola):
	print("Parola Hatalı...")
	pass
elif(kullanıcı_adı!=sys_kullanıcı_adı and parola==sys_parola):
	print("Kullanıcı Adı Hatalı.....")
elif(kullanıcı_adı!=sys_kullanıcı_adı and parola!=sys_parola):
	print("Kullanıcı Adı ve Parola Hatalı...")
elif(kullanıcı_adı==sys_kullanıcı_adı and parola==sys_parola):
	print("Giriş Başarılı.....")
