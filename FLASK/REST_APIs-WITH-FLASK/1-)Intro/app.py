from flask import (
    Flask, # bir Flask uygulaması oluşturmak için
    jsonify, # json return etmek için 
    request # gelen istekleri karşılamak ve içerisinden verileri almak için 
)


app = Flask(__name__) # Flask uygulaması oluşturuyoruz

STORES = [ # dict'lerden oluşan bir liste
    {'name': 'İlk Mağaza',
     'items': [
         {
             'name': 'İlk İtem',
             'price': 9.99
         }
     ]
     }
]


@app.route('/store', methods=['POST']) # /store'a gelen post istekleri karşılar
def create_store():
    request_data = request.get_json() # geleb isteğin içerisindeki json'ı alıyoruz
    new_store = {'name': request_data['name'], 'items': []} # yeni bir dict oluşturuyoruz
    STORES.append(new_store) # STORES listemize yeni oluşturduğumuz dict'i ekliyoruz
    return jsonify(new_store) # oluşturduğumuz yeni dict'i json olarak return ediyoruz


@app.route('/store/<string:name>') # name adında bir parametre alır
def get_store(name): # url'e gelen name
    for store in STORES: # tüm listeyi dön
        if store['name'] == name: # eğer dict'in name key'i url'den gelen name'e eşit ise
            return jsonify(store) # ilgili dict'i return et
    return jsonify({'message': 'Store Not Found!'}) # burası çalışırsa parametre olarak gelen name değişkeni STORES içerisindeki key'lerde bulunamamıştır


@app.route('/store')
def get_stores():
    return jsonify({'stores': STORES}) # tüm dict'leri dön


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in STORES:
        if store['name'] == name: # parametre olarak gelen name o anki dict'in name keyine eşit ise
            new_item = { # yeni bir item oluştur
                'name': request_data['name'], # request_data dict'inin içerisindeki name
                'price': request_data['price'],
            }
            store['items'].append(new_item) # ilgili dict'e yeni oluşturduğun elemanı ekle
            return jsonify(new_item) # ilgili dict'i dön
    return jsonify({'message': 'Store Not Found!'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in STORES:
        if store['name'] == name:
            return jsonify({'items': store['items']}) # name key'i parametre olarak gelen name'e eşit olan dict'in items'ını dön
    return jsonify({'message': 'Store Not Found!'})


if __name__ == '__main__':
    app.run(debug=True)
