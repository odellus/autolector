import requests

url = 'http://127.0.0.1:5005/'

res = requests.get(url)

print("If it worked it will say {'hello':'world!'}")

print(res.json())
