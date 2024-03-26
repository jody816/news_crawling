import requests

r = requests.get("https://naver.com")
with open("naver.txt") as f:
    f.write(r.text)