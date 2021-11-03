import requests

URL = "http://192.168.1.37/.hidden/"

r = requests.get(URL)
for path in r.text.splitlines()[4:-3] :
    lv1_path = path[9:26 + 9 + 1]
    r2 = requests.get(URL + lv1_path)
    readme = requests.get(URL + lv1_path + "README")
    print(readme.text)
    for path2 in r2.text.splitlines()[4:-3] :
        lv2_path = path2[9:26 + 9 + 1]
        r3 = requests.get(URL + lv1_path + lv2_path)
        readme2 = requests.get(URL + lv1_path + lv2_path + "README")
        print(readme2.text)
        for path3 in r3.text.splitlines()[4:-3] :
            lv3_path = path3[9:26 + 9 + 1]
            r4 = requests.get(URL + lv1_path + lv2_path + lv3_path + "README")
            print(r4.text)
