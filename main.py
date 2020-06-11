import requests

try:
    r = requests.get('https://icuse3.bbt.co.id')
    print(r.status_code)
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print("situs bermasalah", e)
