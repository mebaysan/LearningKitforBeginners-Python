import smtplib

host="smtp.gmail.com"     #kullanacağımız sunucuyu host objesine atadık
port=587				  #kullanacağımız portu atadık(google 587 kullanıyor)
username="deneme@gmail.com"  #bu servere bağlanacağımız mail adresş
password="bendenemeşifresiyim"	#şifresi
from_mail=username  		# eposta göndereceksek bunun kimden gideceği
mail_list=["mailgönderilecekler@gmail.com"] # mail gönderileceklerin listesi

email_connection=smtplib.SMTP(host,port) #aynı sql bağlantısındaki gibi bağlantımıza bir değişken atıyoruz
emal_connection.ehlo()					 #bağlantıyı başlatıyoruz
email_connection.starttls()         # bağlantıyı şifreler
email_connection.login(username,password) # sunuculara username ve password objeleri üstünden bağlan
email_connection.sendmail(from_mail,mail_list,"yazıyazılacak")# parametreleri verdik sırasıyla ; gönderen,alan,textMesaage
email_connection.quit()    # bağlantıyı sonlandırıyoruz
