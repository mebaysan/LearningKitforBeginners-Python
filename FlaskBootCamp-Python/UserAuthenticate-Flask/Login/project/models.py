from project import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # String(64) -> en fazla 64 karakter olsun dedik, unique=True -> her user'in email adresi unique olsun, eğer aynı email adresi olursa kabul etmesin
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        # daha kullanıcı oluşturulurken şifresini hashliyoruz
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # kullanıcının şifresini kontrol ediyoruz
        return check_password_hash(self.password_hash, password)
