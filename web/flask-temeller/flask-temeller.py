from flask import Flask,render_template   # flask modülünden Flask fonk çağırdık

	
app = Flask(__name__) 							#Flask(__name__) fonksiyonu ile bir app objesi oluşturduk
@app.route("/")									#hazır decorator kullandık.(@app.route) url istediğimizde route içine ("/url adı")
def index():
	sayı=10	
	sayı2=15												#pythonda işlerimizi fonksiyonlar ile hallettiğimiz için bir ana sayfa fonksiyonu oluşturuyoruz
	return render_template("index.html",number=sayı,number2=sayı2)		#return dersek html sayfası veya herhangi bir string olabilir. buraya bir yazı döndürmek istiyoruz. Oyüzden return kullanmak önemli.Ancak oraya template koymak istersek return render_template("template_adı.html")
												#burada da python kodlarını nasıl webde görüntüleyebileceğimizi öğrendik. sayı objesi oluşturuyoruz ve return_template fonksiyonu içine number=sayı diyerek anahtar kelime belirliyoruz.Html kodlarında yazarken python kodunun gelmesini istediğimiz yere {{}} 2 süslü parantez içine anahtar kelimesini yazıyoruz
												#ÖNEMLİ NOT! BÜTÜN TEMPLATELER templates klasörü altına yazılır. Çünkü flask otomatikmen templates klasörüne bakar
												# {% extends "mirasalınacak_adı.html"	%} bunu yaptığımız zaman kaynak kodlarda index.html içine layout.html'i miras aldığımız için layout.html içindeki kodlar geldi
											
@app.route("/hakkımda")							#flask ile yazarken mutlaka her url adresi için fonksiyon oluşturmalıyız.
def hakkımda():									#hakkımda sayfası için fonksiyon oluşturduk
	article=dict()								#sözlük kullanmak için article diye bir obje oluşturup türünü lsite belirledik
	article["title"]="title key: 'Başlık' value"	# article objemize key&values belirliyoruz.
	article["body"]="body key : 'Yazı' value"		# belirlediğimiz keys&values değerlerini bu urlde göstermek için hakkımda.html adlı bir kaynak kodunu templates içine kaydediyoruz.
	article["author"]="author key : 'Baysan' value"	# bu key'lerin values'lerini bastırmak için hakkımda.html içinde {{article.title}} şeklinde kullanıyoruz. Unutma!: python kodları süslü parantez içinde kullanılır.					
	return render_template("hakkımda.html",article=article)		

"""
blocklar ve inheritence (kalıtım)
index.html dosyasını layout.html dosyasından miras almıştık: {%extends "layout.html"	%}
-----------------------------------------
layout.html dosyasında blocklar oluşturup bu blocklara isim verdik:
{%block deneme%}
<p>Deneme Bloğu</p>
{%endblock deneme%}  		burada bir blok oluşturduk ve sayfada bu yaazının görünmesini sağladık
------------------------------------
Ancak biz index.html sayfasının layout.html'den herşeyi almasını istiyoruz fakat anasayfada "Deneme Bloğu" değilde "Deneme Yazısı" yazmasını istiyoruz;
index.html içine girer;
{%block deneme%}
<p>Deneme Yazısı</p>
{%endblock deneme%} bu şekilde yaparsak, yani herşeyiyle miras almıştık, ve değiştirmek istediğimiz bloğu tekrar açar içini düzenler bloğu tekrar kapatırız.
"""

if __name__=="__main__": 
	app.run(debug=True)  						#debug=True diyerek sitede güncelleme yapmayı sağladık. Kaynak kodda ne değiştirirsen siteye etki ediyor.app.run diyerek yukarda oluşturduğumuz app objesini çalıştırdık.

