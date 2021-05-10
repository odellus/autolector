import requests
import json

# GLOBAL VARIABLES
questions = [
    'How many countries contain rainforest?',
    'How large is the rainforest?',
    'What is another name for the rainforest?',
    'What is another name for the rainforest in English?',
    'What country has the most rainforest?',
    'How many species live in the rainforest?',
    'How many species of animals live in the rainforest?',
    'How many species of plants live in the rainforest?',
    'What country has the second most rainforest?',
    'rainforest is how the large?',
    'name is what another rainforest for the.'
]

context = '''The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; Spanish: Selva Amazónica, Amazonía or usually Amazonia; French: Forêt amazonienne; Dutch: Amazoneregenwoud), also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf forest that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometres (2,700,000 sq mi), of which 5,500,000 square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana. States or departments in four nations contain "Amazonas" in their names. The Amazon represents over half of the planet\'s remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest in the world, with an estimated 390 billion individual trees divided into 16,000 species.'''

port = 5005
service_address = '/api/qa'
url = f'http://127.0.0.1:{port}{service_address}'


# FUNCTIONS
def ask_question(question):
    body = {'question': question, 'context': context}
    body_str = json.dumps(body)
    res = requests.post(url, data=body_str)
    answer = res.json().get('answer')
    return answer

def main():
    print(f'Context: {context}')
    for question in questions:
        print(f'Q: {question}')
        answer = ask_question(question)
        print(f'A: {answer}')

# RUN MAIN
if __name__ == '__main__':
    main()
