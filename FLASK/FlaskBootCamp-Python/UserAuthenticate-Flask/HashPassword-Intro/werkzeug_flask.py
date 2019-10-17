"""
sudo pip3 install Werkzeug
"""
from werkzeug.security import generate_password_hash, check_password_hash

# içeri verilen parametreyi şifreler
hashed_pass = generate_password_hash('çokgizlişifre')
print(hashed_pass)
# ilk parametre hashlenmiş şifre ve 2. parametre kontrol edilecek şifre. Eşleşirse true, eşleşmezse false döner.
check = check_password_hash(hashed_pass, 'çokgizlişifre')
print(check)
