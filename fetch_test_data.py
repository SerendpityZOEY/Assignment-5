import tweepy
from tweepy import OAuthHandler
import time

consumer_key = 'pJIoJeavQRIO8RraY2a7yw2dE'
consumer_secret = 'rFVZ4bTOG8mqVaPDJLuflEI76O4TC63qmGtKNFfgltX8wXktfI'
access_token = '3668395333-YAVJvmDo1WmkEtWJSJrAoSMQXI3XetXWn7984ae'
access_secret = 'jY2hnjDPaUjMqS8DFDID2FLYaUG4M0Fmla23oq4bPz1iQ'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

follower_list = []
for user in tweepy.Cursor(api.followers, screen_name="cnnbrk").items():
    follower_list.append(user.screen_name)
    if len(follower_list) > 50:
        break

active_user = {}

for u in follower_list:
    user = api.get_user(u)
    active_user[user.screen_name] = {}
    active_user[user.screen_name]['tweets'] = user.statuses_count
    active_user[user.screen_name]['followers'] = user.followers_count

import json

with open('./data/test.json', 'w') as f:
    json.dump(active_user, f)
