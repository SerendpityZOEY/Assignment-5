import tweepy
from tweepy import OAuthHandler
import time
import OSC

consumer_key = 'pJIoJeavQRIO8RraY2a7yw2dE'
consumer_secret = 'rFVZ4bTOG8mqVaPDJLuflEI76O4TC63qmGtKNFfgltX8wXktfI'
access_token = '3668395333-YAVJvmDo1WmkEtWJSJrAoSMQXI3XetXWn7984ae'
access_secret = 'jY2hnjDPaUjMqS8DFDID2FLYaUG4M0Fmla23oq4bPz1iQ'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

users = tweepy.Cursor(api.followers, screen_name="cnnbrk").items()

def sendToWekinator(tweets, followers):
    send_address = '127.0.0.1', 6448

    c = OSC.OSCClient()
    c.connect(send_address)  # set the address for all following messages

    try:
        rNum = OSC.OSCMessage()
        rNum.setAddress("/wek/inputs")
        rNum.append(tweets)
        rNum.append(followers)
        c.send(rNum)
        print "Sent one user..."
        print rNum
        time.sleep(1)  # wait here 1 second

    except KeyboardInterrupt:
        print "Closing OSCClient"
        c.close()
        print "Done"

while True:
    try:
        u = users.next()
        user_name = u.screen_name
        user = api.get_user(user_name)
        sendToWekinator(user.statuses_count, user.followers_count)
        # Insert into db
    except tweepy.TweepError:
        time.sleep(15*60)
        continue
    except StopIteration:
        break
