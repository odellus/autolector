import json
import time
from flask import Flask, request
from flask_restful import Resource, Api
from transformers import pipeline

# Initialize API.
app = Flask(__name__)
api = Api(app)

# Load question answering model.
def load_model():
    print(' * Loading model...')
    start = time.time()
    nlp = pipeline('question-answering', model='distilbert-base-cased-distilled-squad')
    print(f' * Model loaded in {time.time()-start} seconds!')
    return nlp

# Do this outside of the QuestionAnsweringApi class to load only once.
nlp = load_model()

class QuestionAnsweringApi(Resource):
    def get(self):
        return {
            'question':'The question to be asked.',
            'context': 'The context for the question.'
            }
    def post(self):
        inputs = request.get_json(force=True)
        question, context = inputs.get('question'), inputs.get('context')
        result = nlp(question=question, context=context)
        answer = result['answer']
        return {'answer': answer}

api.add_resource(QuestionAnsweringApi, '/')
port = 5000

if __name__ == '__main__':
    app.run(debug=True, port=port)
