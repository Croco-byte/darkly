import requests

parameters = {'sujet': 2, 'valeur': 100000}
r = requests.post('http://192.168.1.20/?page=survey', data=parameters)
print(r.text)
