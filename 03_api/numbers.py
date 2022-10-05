# Numbers api: http://numbersapi.com/

import requests

url = "http://numbersapi.com"

year = input("Enter a year: ")

url = url + "/" + year + "/year"

response = requests.request("GET", url)

print(response.text)
