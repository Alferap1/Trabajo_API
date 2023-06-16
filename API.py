import requests

user_agent = {'User-agent': 'Mozilla/5.0'}
url = "https://api.impel.io/spin/carros/u-23420?v=20160212"
r = requests.get(url, headers=user_agent)

print(r.json())
