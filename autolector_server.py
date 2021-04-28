import json
import time
import logging
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from urllib.parse import parse_qs
from transformers import (
    pipeline,
    DistilBertTokenizerFast,
    DistilBertForQuestionAnswering
    )
# Out local package
from autolector_db import AutolectorDB

# Set up logger.
logging.basicConfig(
    filename='autolector.log',
    level=logging.DEBUG
    )
logging.debug('This should go to the file!')

db = AutolectorDB()

# Initialize API.
app = Flask(__name__)
CORS(app)
api = Api(app)

# Load question answering model.
def load_model():
    '''
    Create a transformers pipeline for question answering inference.
    '''
    msg = ' * Loading model...'
    logging.info(msg)
    model_dir = 'models'
    model_name = 'distilbert-base-cased-distilled-squad'
    model_path = f'./{model_dir}/{model_name}'
    msg = f'Model loaded from {model_path}'
    logging.info(msg)
    start = time.time()
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
    model = DistilBertForQuestionAnswering.from_pretrained(model_path)
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    msg = f' * Model loaded in {time.time()-start} seconds!'
    logging.info(msg)
    return nlp

class AutolectorApi(Resource):
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
        result = nlp(question=question, context=context)
        answer = result['answer']
        logging.info(question)
        logging.info(context)
        logging.info(answer)
        db.insert(question, context, answer)
        return {'answer': answer}

# api
api.add_resource(AutolectorApi, '/qa')
port = 5000

if __name__ == '__main__':
    # Do this outside of the QuestionAnsweringApi class to load only once.
    nlp = load_model()
    app.run(debug=True, port=port)
