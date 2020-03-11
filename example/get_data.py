import requests

url = "https://cvapi.awal.pw/"
response = requests.request("GET", url)
print(response.text.encode('utf8'))
