import requests
r = requests.get('http://10.211.203.91:3000/randomfact')
result = r.json()
print(result)

