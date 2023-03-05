import requests
URL = "https://www.lipsum.com/"
r = requests.get(URL)
print(r.content)
