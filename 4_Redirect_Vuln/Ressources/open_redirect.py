import requests

r = requests.get('http://192.168.1.37/index.php?page=redirect&site=http://192.168.1.5:8888')
print(r.text)
