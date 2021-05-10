import requests
import json

port = 5005
url = f'http://127.0.01:{port}/'

def get_body():
    return {'input': 'This Is The sTrInG we want in lowEr CAsE.'}

def main():
    body = get_body()
    print('This is the input to our API.')
    print(body)

    # We have to serialize the body of our post request before we can send.
    body_str = json.dumps(body)

    # Don't believe me? Uncomment the line below this one!
    # res = requests.post(url, data=body)

    # This is us passing the serialized body.
    res = requests.post(url, data=body_str)
    print('This is the output from the API.')
    print(res.json())

if __name__ == '__main__':
    main()
