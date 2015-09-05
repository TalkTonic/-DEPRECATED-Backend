import requests
import json

payload = {'username': 'matt', 'password': 'lee'}

r = requests.post('https://64b4c509.ngrok.io/conversations', data=payload)
# r = requests.post('http://localhost:5000/conversations', data=payload)
print r.text