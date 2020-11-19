import sqlite3
from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = "select * from users where username=?"
        # unutmayalım query'e giden parametreler tuple olarak gider
        result = cursor.execute(query, (username,))
        row = result.fetchone()  # dönen ilk satırı al eğer boşsa None döner
        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None
        conn.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = "select * from users where id=?"
        # unutmayalım query'e giden parametreler tuple olarak gider
        result = cursor.execute(query, (_id,))
        row = result.fetchone()  # dönen ilk satırı al eğer boşsa None döner
        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None
        conn.close()
        return user


class UserRegister(Resource):
    # bu sınıfa özel bir parser oluşturuyoruz, bu sayede tüm metodlarda aynı fonksiyonları yazmak zorunda kalmayacağız
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True,
                        type=str, help='Username is important!')
    parser.add_argument('password', required=True,
                        type=str, help='Password is important!')

    def post(self):
        # parse_args() fonksiyonu çalıştığında varsa hatalar döner
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {'message': 'Username has already taken!'}, 400
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        query = "INSERT INTO users values (null, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        conn.commit()
        conn.close()

        return {'message': 'User created successfully'}, 201
