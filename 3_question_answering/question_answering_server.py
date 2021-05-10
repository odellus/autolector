import json
from flask import Flask, request
from flask_restful import Resource, Api

from transformers import (
    pipeline,
    DistilBertTokenizerFast,
    DistilBertForQuestionAnswering
)

app = Flask(__name__)
api = Api(app)

def load_model():
    model_dir = '../models'
    model_name = 'distilbert-base-cased-distilled-squad'
    model_path = f'./{model_dir}/{model_name}'
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
    model = DistilBertForQuestionAnswering.from_pretrained(model_path)
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    return nlp

class QuestionAnsweringApi(Resource):
    def post(self):
        inputs = request.get_json(force=True)
        question = inputs.get('question')
        context = inputs.get('context')
        result = nlp(question=question, context=context)
        answer = result['answer']
        return {'answer': answer}

api.add_resource(QuestionAnsweringApi, '/api/qa')
port = 5005

if __name__ == '__main__':
    nlp = load_model()
    app.run(debug=True, port=port)
