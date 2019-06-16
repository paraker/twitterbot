import tweepy
import json

with open('keys.json', 'r') as keys:
    keys = json.load(keys)

# Auth to twitter
auth = tweepy.OAuthHandler(
    keys['consumer_api_key'],
    keys['consumer_api_secret']
)
auth.set_access_token(
    keys['access_token'],
    keys['access_secret']
)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication successful")
except BaseException as e:
    print(f"Error during auth: {e}")


# if __name__ == '__main__':
#