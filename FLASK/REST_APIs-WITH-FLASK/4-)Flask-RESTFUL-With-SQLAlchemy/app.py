from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.secret_key = '$baba$naber#-_-'
# veritabanının adresi
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # SQLAlchemy ile Flask'ı bind ediyoruz
api = Api(app)


@app.before_first_request  # uygulamaya ilk istek atılmadan önce
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
