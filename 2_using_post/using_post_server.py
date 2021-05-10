from flask import Flask, request
from flask_restful import Resource, Api

print(f'__name__ in this context is just{__name__}, should be name of file.')
app = Flask(__name__)
print(f'We are loading up a Flask app')
api = Api(app)

def callback(input_str):
    return input_str.lower()

class UsingPostApi(Resource):
    def get(self):
        return {'hello': 'world!'}
    def post(self):
        data = request.get_json(force=True)
        print(data)
        input_str = data.get('input')
        output_str = callback(input_str)
        res = {'output': output_str}
        return res

api.add_resource(UsingPostApi, '/')
port = 5005

if __name__ == '__main__':
    app.run(debug=True, port=port)
