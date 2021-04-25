import requests
import json
from pprint import pprint
from io import StringIO


question = 'Which name is also used to describe the Amazon rainforest in English?'

context = '''The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; Spanish: Selva Amazónica, Amazonía or usually Amazonia; French: Forêt amazonienne; Dutch: Amazoneregenwoud), also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf forest that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometres (2,700,000 sq mi), of which 5,500,000 square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana. States or departments in four nations contain "Amazonas" in their names. The Amazon represents over half of the planet\'s remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest in the world, with an estimated 390 billion individual trees divided into 16,000 species.'''

url = 'http://127.0.0.1:5000'

def question_answering_client(question, context, url=url):
    '''
    A simple client function for our question answering API.
    '''
    data = {'question': question, 'context': context}
    body = json.dumps(data)
    result = requests.post(url, data=body)
    return result.json().get('answer')

def get_indented_context(context):
    '''
    Indent the context for easier readability.
    '''
    context_stream = StringIO()
    pprint(context, stream=context_stream, indent=0, width=60)
    context_str = context_stream.getvalue()
    # pprint puts text in parenthesis and adds newlines to the end.
    return context_str.replace('\'', '').replace('\n', '\n\t')[1:-3]

if __name__ == "__main__":
    answer = question_answering_client(question, context)
    indented_context = get_indented_context(context)
    print(f'Context:\n\t {indented_context}\n')
    print(f'Question:\n\t{question}')
    print(f'Answer:\n\t{answer}.')
