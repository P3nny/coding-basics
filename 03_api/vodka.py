import requests

url = "https://the-cocktail-db.p.rapidapi.com/search.php"

querystring = {"s":"vodka"}

headers = {
	"X-RapidAPI-Key": "4826c20b69msh228b3013cc5220ep1f231ejsn9778841c66f0",
	"X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)