import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True,
                        type=str, help='Username is important!')
    parser.add_argument('password', required=True,
                        type=str, help='Password is important!')

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': 'Username has already taken!'}, 400
        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {'message': 'User created successfully'}, 201
