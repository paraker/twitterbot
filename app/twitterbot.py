import tweepy
import json


class TwitterBot:
    def __init__(self, keys):
        self._keys = keys
        self._auth = None
        self.api = None
        self.timeline = None

        self.twitter_auth()
        self.create_api_object()

    def twitter_auth(self):
        # Authenticate to Twitter
        self._auth = tweepy.OAuthHandler(
            self._keys['consumer_api_key'],
            self._keys['consumer_api_secret']
        )
        self._auth.set_access_token(
            self._keys['access_token'],
            self._keys['access_token_secret']
        )

    def create_api_object(self):
        # Create API object. If twitter rate limit is applied, wait and print a message for us!
        self.api = tweepy.API(self._auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def verify_twitter_credentials(self):
        try:
            self.api.verify_credentials()
            return "Authentication successful"
        except BaseException as e:
            return f"Error during auth: {e}"

    def print_home_timeline(self):
        self.timeline = self.api.home_timeline()
        for tweet in self.timeline:
            print(f'{tweet.user.name} said {tweet.text}')


if __name__ == '__main__':
    # Read authentication keys
    with open('keys.json', 'r') as file:
        auth_keys = json.load(file)

    # Create twitterbot object
    twitter_bot = TwitterBot(auth_keys)

    # Check credentials
    print(twitter_bot.verify_twitter_credentials())

    # Get my profile's timeline's latest tweets
    twitter_bot.print_home_timeline()

    # Create a tweet from a python string
    # twitter_bot.api.update_status("Test Tweet from Tweepy Python")

    # get_user() returns an object containing user details.
    # This returned object also has methods to access information related to the user.
    user = twitter_bot.api.get_user('perry430')
    print(user.name, user.description, user.location)
    for follower in user.followers():
        print(follower.name)

    # Like the most recent tweet on your timeline
    latest_tweet = twitter_bot.timeline[0]
    # twitter_bot.api.destroy_favorite(latest_tweet.id)
    print(twitter_bot.api.favorites())