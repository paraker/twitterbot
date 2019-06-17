# Twitterbot
Load your twitter API keys into keys.json under /app

# Names
* A status is a tweet. 
* A friendship is a follow-follower relationship.
* A favorite is a like.

# API object methods
Some sample methods used in this project

* Method for user timelines

        api.home_timeline()
        
* Method for new tweets

        api.update_status(<string>)
    
* Method for users

        api.get_user(<user>)

# Stream listener
Stream listener is used to listen for keywords, anywhere on twitter.