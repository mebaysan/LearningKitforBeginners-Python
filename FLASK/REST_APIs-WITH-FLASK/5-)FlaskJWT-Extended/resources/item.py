from flask_restful import Resource, reqparse
from flask import request
from models.item import ItemModel
from flask_jwt_extended import jwt_required, get_jwt_claims, jwt_optional, get_jwt_identity, fresh_jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        required=True,
                        type=float,
                        help='Price field is cannot be left blank!')

    parser.add_argument('store_id',
                        required=True,
                        type=int,
                        help='Every item needs a store id')

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}

    @fresh_jwt_required
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f"An item with name '{name}' already exists"}, 400
        data = Item.parser.parse_args()
        item = ItemModel(
            name=name, price=data['price'], store_id=data['store_id'])
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occured inserting the item'}, 500
        return item.json(), 201

    @jwt_required
    def delete(self, name):
        claims = get_jwt_claims()
        if not claims['is_admin']:  # eğer claims içinde is_admin False ise
            return {'message': 'Admin privilege required'}, 401
        item = ItemModel.find_by_name(name)
        if not item:
            return {'message': 'Item Not Found'}, 400
        item.delete_from_db()
        return {'message': f'Item ({name}) deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'], data['store_id'])
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        items = [item.json() for item in ItemModel.find_all()]
        if user_id:  # eğer user login olmuşsa itemların tüm özellikleri
            return {'items': items}, 200
        else:
            return {'items': [item['name'] for item in items], 'message': 'More data available if you log in'}, 200
