from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from flask import request


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        required=True,
                        type=float,
                        help='Price field is cannot be left blank!')

    @classmethod
    def find_by_name(cls, name):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = "SELECT * FROM items where name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        conn.close()
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    @classmethod
    def insert(cls, name, price):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = "insert into items values (?, ?)"
        cursor.execute(query, (name, price))
        conn.commit()
        conn.close()

    @classmethod
    def update(cls, name, price):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = "update items set price=? where name=?"
        cursor.execute(query, (price, name))
        conn.commit()
        conn.close()

    @jwt_required()
    def get(self, name):
        item = Item.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}

    def post(self, name):
        if Item.find_by_name(name):
            return {'message': f"An item with name '{name}' already exists"}, 400
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        try:
            Item.insert(item['name'], item['price'])
        except:
            return {'message': 'An error occured inserting the item'}, 500
        return item, 201

    def delete(self, name):
        if not Item.find_by_name(name):
            return {'message': 'Item Not Found'}, 400
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = "delete from items where name = ?"
        cursor.execute(query, (name,))
        conn.commit()
        conn.close()
        return {'message': f'Item ({name}) deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        if Item.find_by_name(name):
            try:
                Item.update(name, data['price'])
            except:
                return {'message': 'An error occured inserting the item'}, 500
        else:
            try:
                Item.insert(name, data['price'])
            except:
                return {'message': 'An error occured updating the item'}, 500
        return Item.find_by_name(name)


class ItemList(Resource):
    def get(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = "select * from items"
        items = []
        for row in cursor.execute(query):
            items.append({'name': row[0], 'price': row[1]})
        conn.close()
        return {'items': items}, 200
