import requests

url = "https://catfact.ninja/fact"

response = requests.request("GET", url)

print(response.json()["fact"])
