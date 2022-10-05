# http://universities.hipolabs.com/search?country=United+States

import requests

url = "http://universities.hipolabs.com/search"

country = input("Enter a country: ")

url = url + "?country=" + country

print(url)

response = requests.request("GET", url)

print(url, response.json()[0])

with open("universities.json", "w") as f:
    f.write(str(response.json()))
