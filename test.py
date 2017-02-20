import json
import OSC
import time
import argparse

parser = argparse.ArgumentParser(description='Indicate file to read')
parser.add_argument('--file', type=str, default="active",
                        help="Indicate file to read")
args = parser.parse_args()
st = 1
if args.file == 'active':
    with open('./data/active.json') as data_file:
        data = json.load(data_file)
elif args.file == 'inactive':
    with open('./data/inactive.json') as data_file:
        data = json.load(data_file)
else:
    with open('./data/test.json') as data_file:
        data = json.load(data_file)
        st = 1

print "*******"
print "This program sends 3 random inputs to Wekinator every second."
print "Default is port 6448, message name /wek/inputs"
print "If Wekinator is not already listening for OSC, we will get an error."
print "*******"

send_address = '127.0.0.1', 6448

# OSC basic client
c = OSC.OSCClient()
c.connect(send_address)  # set the address for all following messages

# lets try sending a different random number every frame in a loop
while 1:
    try:
        for key, value in data.iteritems():
            rNum = OSC.OSCMessage()
            rNum.setAddress("/wek/inputs")
            rNum.append(float(value['tweets']))
            rNum.append(float(value['followers']))
            c.send(rNum)
            print "Sent one user...(Number of tweets, Number of followers)"
            print rNum
            rNum.clearData()
            time.sleep(st)  # wait here 1 second

    except KeyboardInterrupt:
        print "Closing OSCClient"
        c.close()
        print "Done"


