import tweepy
import os


class TwitterBot:
    def __init__(self):
        self._auth = None
        self.api = None
        self.timeline = None
        self.tweets_listener = None
        self.stream = None
        self._keys = dict()
        self._keys['consumer_key'] = os.getenv('CONSUMER_KEY')
        self._keys['consumer_secret'] = os.getenv('CONSUMER_SECRET')
        self._keys['access_token'] = os.getenv('ACCESS_TOKEN')
        self._keys['access_token_secret'] = os.getenv('ACCESS_TOKEN_SECRET')

    def __repr__(self):
        return f'Class object of class: {self.__class__.__name__}'

    def twitter_auth(self):
        # Authenticate to Twitter
        self._auth = tweepy.OAuthHandler(
            self._keys['consumer_key'],
            self._keys['consumer_secret']
        )
        self._auth.set_access_token(
            self._keys['access_token'],
            self._keys['access_token_secret']
        )

    def create_api_object(self):
        # Create API object. If twitter rate limit is applied, wait and print a message for us!
        self.api = tweepy.API(
            self._auth,
            wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True
        )

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

    def start_stream_listener(self):
        self.tweets_listener = MyStreamListener(self.api)  # Instantiate stream listener
        self.stream = tweepy.Stream(self.api.auth, self.tweets_listener)  # Instantiate Stream


class MyStreamListener(tweepy.StreamListener):
    """
    On run: event loop style stream listener printing matched tweets to stdout
    """

    def __init__(self, api):
        self.api = api
        self.me = api.me()
        self.counter = 0

    def on_status(self, tweet):
        print(f'{tweet.user.name}:{tweet.text}')
        self.counter += 1
        self.news = None
        if self.counter > 3:
            return False

    def on_error(self, status_code):
        if status_code == 420:
            return False
        print('error detected')


if __name__ == '__main__':
    twitter_bot = TwitterBot()  # Create twitterbot object
    twitter_bot.twitter_auth()  # Auth with twitter
    twitter_bot.create_api_object()  # Create api object

    # Check credentials
    print(twitter_bot.verify_twitter_credentials())

    # Get my profile's timeline's latest tweets
    # twitter_bot.print_home_timeline()

    # Create a tweet from a python string
    # twitter_bot.api.update_status("Test Tweet from Tweepy Python")

    # get_user() returns an object containing user details.
    # This returned object has methods to access information related to the user.

    # user = twitter_bot.api.get_user('perry430')
    # print(user.name, user.description, user.location)
    # for follower in user.followers():
    #     print(follower.name)

    # Like the most recent tweet on your timeline
    # latest_tweet = twitter_bot.timeline[0]  # Find latest tweet
    # twitter_bot.api.create_favorite(latest_tweet.id)  # Like the latest tweet
    # twitter_bot.api.destroy_favorite(latest_tweet.id)  # remove like from latest tweet
    # print(twitter_bot.api.favorites())  # List liked tweets?

    # Start a listener for global tweets. Filter on given words and language. Prints to stdout.
    twitter_bot.start_stream_listener()  # Pass our api object to the stream listener class
    twitter_bot.stream.filter(track=['burger', 'Burger'], languages=['en'])  # Starts the stream listener.
    # matches on the keywords go to the "twitter_bot.stream.on_status()" function for processing.
