import json
import time
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from urllib.parse import parse_qs
from transformers import (
    pipeline,
    DistilBertTokenizerFast,
    DistilBertForQuestionAnswering
    )

# Initialize API.
app = Flask(__name__)
CORS(app)
api = Api(app)

# Load question answering model.
def load_model():
    '''
    Create a transformers pipeline for question answering inference.
    '''
    print(' * Loading model...')
    model_dir = 'models'
    model_name = 'distilbert-base-cased-distilled-squad'
    model_path = f'./{model_dir}/{model_name}'
    start = time.time()
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
    model = DistilBertForQuestionAnswering.from_pretrained(model_path)
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    print(f' * Model loaded in {time.time()-start} seconds!')
    return nlp

class QuestionAnsweringApi(Resource):
    '''
    Class to describes get, post, etc.. methods of our RESTful
    question answering API. Inheirits flask_restful.Resource.
    '''
    def get(self):
        return 'Send a POST request with the form \
        { question: Question being asked, context: Document containing answer }'

    def post(self):
        '''
        POST method. Body of POST request must be in JSON format with schema:
            { question: Question being asked,
              context: Document containing answer }
        Returns a JSON object with schema:
            { answer: Answer to question extracted from context}
        '''
        inputs = request.get_json(force=True)
        question = parse_qs(inputs['question'])['question'].pop()
        context = parse_qs(inputs['context'])['context'].pop()
        print(question)
        print(context)
        result = nlp(question=question, context=context)
        answer = result['answer']
        print(answer)
        return {'answer': answer}

# api
api.add_resource(QuestionAnsweringApi, '/qa')
port = 5000

if __name__ == '__main__':
    # Do this outside of the QuestionAnsweringApi class to load only once.
    nlp = load_model()
    app.run(debug=True, port=port)
