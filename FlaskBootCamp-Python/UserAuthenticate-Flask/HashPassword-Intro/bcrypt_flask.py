"""
sudo pip3 install flask-bcrypt
"""
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()  # instance oluşturduk

password = 'çokgizlişifre'

hashed_password = bcrypt.generate_password_hash(password)  # şifreyi şifreledik
print(hashed_password)

# hashlenmiş şifre(1. parametre) ile uyuşması gereken şifreyi(2.parametre) veriyoruz. Eğer uyuşursa True uyuşmazsa false döner
check = bcrypt.check_password_hash(hashed_password, password)
print(check)
