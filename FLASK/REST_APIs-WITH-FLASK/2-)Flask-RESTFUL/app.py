from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = '$baba$naber#-_-'
api = Api(app)  # ana flask uygulamamızın üzerine bir api oluşturuyoruz

# /auth endpointi oluşturur ve username ile password bekler. Gönderdiğimiz değerleri authenticate fonksiyonuna yollar oradan bir user dönerse JWT oluşur ve identity fonksiyonuna gönderir
jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):  # Api için modellerimizi oluştururken Resource sınıfından inherit alırız
    # jwt yok ise bu endpoint çalışmayacak. Bunun için header'da Authorization key'inin karşısına "JWT [TOKEN]" value'sini eklememiz gerekmektedir
    @jwt_required()
    def get(self, name):  # Resource metodları birer dict dönmelilerdir
        # ilk parametre hangi fonksiyon çalışacak, hangi liste üzerinde (filter), bulduğu ilk elemanı döner eğer bulamazsa None döner (next)
        item = next(filter(lambda x: x['name'] == name, items), None)
        # eğer item varsa 200, yoksa (None) 404
        return {'item': item}, 200 if item else 404

    def post(self, name):  # Resource metodları parametre olarak url'e eklenen parametreleri yakalarlar, request içerisinde gelen verileri flask'dan request ile yakalarız
        # atılan request'in content-type'ı application/json olmalıdır
        if next(filter(lambda x: x['name'] == name, items), None) != None:
            return {'message': f"An item with name '{name}' already exists"}, 400
        request_json = request.get_json()
        # request_json = request.get_json(silent=True) # atılan request'in content-type'ı application/json değilse hata değil none döner
        # request_json = request.get_json(force=True) # atılan request'in content-type'ı application/json olma zorunluluğu ortadan kalkar
        price = request_json['price']
        item = {'name': name, 'price': price}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items  # en üstte tanımladığımız GLOBAL items değişkenini burada kullanacağız
        items = list(filter(lambda x: x['name'] != name, items)),
        return {'message': f'Item ({name}) deleted'}

    def put(self, name):
        parser = reqparse.RequestParser()  # parser objesi oluşturuyoruz
        parser.add_argument('price',  # request body'den yakalamak istediğimiz parametreyi parser'a ekliyoruz
                            required=True,  # bu parametre eksik olabilir mi
                            type=float,  # gelen değer hangi tipe convert olacak
                            help='Price field is cannot be left blank!')  # help -> parametre eksik olursa ne mesaj döneceği
        # parser içerisinde request'ten yakaladığımız key-value'ları değişkene atıyoruz
        data = parser.parse_args() # hatalar bu fonksiyon çağrıldığında tetiklenir
        # request_json = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            # bir sözlüğü başka bir sözlük ile güncelliyoruz (key'leri aynı olmalı)
            item.update(data)
        return item


class ItemList(Resource):  # sadece tüm itemları dönmek için bir Resource oluşturuyoruz
    def get(self):
        return {'items': items}, 200


# ilk parametre API'mize eklenecek olan Resource, ikinci parametre ise Resource ulaşmamızı sağlayacak url
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')  # hangi Resource, hangi url

if __name__ == '__main__':
    app.run(debug=True)
