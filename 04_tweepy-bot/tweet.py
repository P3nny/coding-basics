import tweepy
import requests

# cat fact api
url = "https://catfact.ninja/fact"


def get_cat_fact():
    response = requests.request("GET", url)
    return response.json()["fact"]


# Twitter api secrets - these are random strings, they will not work
# You will have to generate your own
CONSUMER_KEY = "pyRgKFq5WAQsD8AXEGmL5w10l"
CONSUMER_SECRET = "iqgZn2v2ZHSz4cpkJSjea0P6prmlxbrjGARANjEkgEPuqC62H3"
BEARER_TOKEN = "BAAAAAAAAAAAAAAAAAAAAM2vgwEAAAAAI5JhdioZVRgNHE%2BEJvf9N2BTo5o%3DHvziWUSC3YoLpESy6sbivUDaNOfYLprAUP6m2SDR85f9MPrvcw"
ACCES_TOKEN = "85112647-kHHzQUuHq54bfdts9d7KPJZsvdpBjEuI34xdIkLC2"
ACCESS_TOKEN_SECRET = "kkKVAxJwZyZ7GKhUdCpaKeKYcplE23ZHRsovVBVUt87St"

CLIENT_ID = "mnB2V1BaWjZjZW51UGdUSGFNUVM6MTpjaQ"
CLIENT_SECRET = "u10gml93rBErQEPa9_plAMTeRZ2mnbyz08tS8-aQGUsEk_rgDQ"

client = tweepy.Client(
    BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCES_TOKEN, ACCESS_TOKEN_SECRET
)

me = client.get_me()
print(me)

last_mention_answered = None

with open("last_mention_save.txt", "r") as f:
    last_mention_answered = f.read().strip()

print(last_mention_answered)

resp = client.get_users_mentions(me.data.id, since_id=last_mention_answered)

print(resp)

if resp.data is None:
    print("No new mentions")
    exit()

for tweet in resp.data:
    catfact = get_cat_fact()
    client.create_tweet(text=catfact, in_reply_to_tweet_id=tweet.id)

    print("Replied to tweet: " + tweet.text)
    print("Tweeted: " + catfact)

with open("last_mention_save.txt", "w") as f:
    f.write(str(resp.data[-1].id))
