from flask import Flask
# pip install flask-restful
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):  # bir class
    def get(self):  # get methodu gelirse
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')  # / -> bu url'e istek gelirse

if __name__ == "__main__":
    app.run(debug=True)
