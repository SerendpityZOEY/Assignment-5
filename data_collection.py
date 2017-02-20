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
users = tweepy.Cursor(api.followers, screen_name="cnnbrk").items()

while True:
    print(len(follower_list))
    if len(follower_list) >= 300:
        break
    try:
        u = users.next()
        follower_list.append(u.screen_name)
        # Insert into db
    except tweepy.TweepError:
        time.sleep(15*60)
        continue
    except StopIteration:
        break

print(len(follower_list))
active_user = {}
inactive_user = {}
for u in follower_list:
    user = api.get_user(u)
    if user.statuses_count > 30 and user.followers_count > 10:
        active_user[user.screen_name] = {}
        active_user[user.screen_name]['tweets'] = user.statuses_count
        active_user[user.screen_name]['followers'] = user.followers_count
    else:
        inactive_user[user.screen_name] = {}
        inactive_user[user.screen_name]['tweets'] = user.statuses_count
        inactive_user[user.screen_name]['followers'] = user.followers_count


print('active', active_user)
print('inactive', inactive_user)

import json

with open('./data/active.json', 'w') as f:
    json.dump(active_user, f)

with open('./data/inactive.json', 'w') as f:
    json.dump(inactive_user, f)
