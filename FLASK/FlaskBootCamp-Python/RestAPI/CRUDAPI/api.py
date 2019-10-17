from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

ponnies = list()


class PonnyNames(Resource):
    def get(self, name):
        for pon in ponnies:
            if pon['name'] == name:
                return pon

        return {'name': None}, 404

    def post(self, name):
        pon = {'name': name}
        ponnies.append(pon)
        return pon

    def delete(self, name):
        for ind, pon in enumerate(ponnies):
            if pon['name'] == name:
                deleted_pon = ponnies.pop(ind)
                print(f"{deleted_pon} is deleted")
                return {'note': 'delete success'}


class AllNames(Resource):
    def get(self):
        return {'ponnies': ponnies}


api.add_resource(PonnyNames, '/ponny/<string:name>')
api.add_resource(AllNames, '/ponnies')
if __name__ == "__main__":
    app.run(debug=True)
