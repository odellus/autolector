from flask import Flask, request
from flask_restful import Resource, Api

print(f'__name__ in this context is just{__name__}, should be name of file.')
app = Flask(__name__)
print(f'We are loading up a Flask app')
api = Api(app)

class HelloWorldApi(Resource):
    def get(self):
        return {'hello': 'world!'}

api.add_resource(HelloWorldApi, '/')
port = 5005

if __name__ == '__main__':
    app.run(debug=True, port=port)
