from keys import *

import tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

api = tweepy.API(auth)

# This will get the last 20 tweets, latest most recent at position 0
# dump = api.home_timeline()

# Add a count param to get up to 200 tweets
# dump = api.home_timeline(count=200)

# Most recent tweet is found with:
# most_recent_id = dump[0].id

# Tweets since last check is found with
# new_tweets = api.home_timeline(since_id=most_recent_id)

# Fun things to do with tweet objects
# dump[0].user.name
# dump[0].text
# dump[0].created_at # returns a datetime.datetime(etc)