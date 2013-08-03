import datetime

from twitter import *

from keys import *

"""This method uses the REST API"""
t=Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# dump = t.statuses.home_timeline()

"""This method uses the streaming API"""
ts=TwitterStream(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# iterator = ts.statuses.sample()
# for i in range(10):
#     print iterator