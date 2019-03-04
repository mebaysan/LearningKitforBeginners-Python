import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host="smtp.gmail.com"
port=587
username="menesbaysan@gmail.com"
password=""
from_email=username
to_email="menesbaysan@gmail.com"   #listeye mail göndermez

message=MIMEMultipart("alternative")
message["Subject"]="SMTP Mail Gönderme Denemeleri"
message["From"]=from_email
message["To"]=to_email
text="Deneme yapıyoruz ancak arada bir yanılıyoruz :)"
text=MIMEText(text,"plain")
message.attach(text)

try:
    connect=smtplib.SMTP(host,port)
    connect.ehlo()
    connect.starttls()
    connect.login(username,password)
    connect.sendmail(from_email,to_email,message.as_string())
    connect.close()
    print("Mail başarıyla gönderildi...")
except:
    print("Mail gönderilemedi...")