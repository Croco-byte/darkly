from multiprocessing import Pool
import hashlib
import sys

if (len(sys.argv) != 3) :
    print ('Usage : python3 md5decrypt.py <MD5 HASH> <WORDLIST>')
    sys.exit(1)

user_hash   = sys.argv[1]
filename    = sys.argv[2]

def bruteforce_hash(password, md5_hash = user_hash) :
    password = password.rstrip()
    guess = hashlib.md5(password.encode()).hexdigest()
    if (guess == md5_hash) :
        print(f"[+] Found working password : {password}")

with open(filename, 'r', errors='replace') as wordlist :
    passwords = wordlist.readlines()

    with Pool(4) as pool :
        results = pool.map(bruteforce_hash, passwords)


