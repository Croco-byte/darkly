import requests

parameters = {'txtName': "script", 'mtxtMessage': 'script', 'btnSign': 'Sign+Guestbook'}

r = requests.post('http://192.168.1.20/?page=feedback', data=parameters)
print(r.text)
