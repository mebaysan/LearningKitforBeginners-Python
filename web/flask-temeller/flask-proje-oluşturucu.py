
dosya=open("/root/Masaüstü/flask-projesi.py","w",encoding="UTF-8")
dosya.write("""
from flask import Flask,render_template

app = Flask(__name__)




if __name__=="__main__":
		app.run(debug=True)
	""")
dosya.close()
print("Projeniz /root/Masaüstü dizinine flask-projesi.py olarak oluştu")