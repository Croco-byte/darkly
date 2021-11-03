import requests

r = requests.get('http://192.168.1.20/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c', headers={"Referer": "https://www.nsa.gov/", "User-Agent": "ft_bornToSec"})
print(r.text)
