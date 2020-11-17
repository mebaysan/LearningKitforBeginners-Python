from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)  # ana flask uygulamamızın üzerine bir api oluşturuyoruz

items = []


class Item(Resource):  # Api için modellerimizi oluştururken Resource sınıfından inherit alırız
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


class ItemList(Resource):  # sadece tüm itemları dönmek için bir Resource oluşturuyoruz
    def get(self):
        return {'items': items}, 200


# ilk parametre API'mize eklenecek olan Resource, ikinci parametre ise Resource ulaşmamızı sağlayacak url
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')  # hangi Resource, hangi url

if __name__ == '__main__':
    app.run(debug=True)
