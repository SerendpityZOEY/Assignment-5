Assignment-5

Using machine learning technique to identify zombie users from the followers of an account

Demo: Demo video can be found within this repo.

Github URL: https://github.com/SerendpityZOEY/Assignment-5

User Story: There're many 'zombie' users exist on social networks. Most of these users are registered by machine rather than a real human. Therefore, if you want to clean these inactive followers of your account, you will need this script to help you identify these users automatically.

First time setup:

Operating system: OSX Python 2.7 That's it!

Open your terminal and type:

pip install tweepy

You can use my authentication key for twitter api but I strongly recommend you to replace it with yours. Here's a tutorial about how to do this: https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/

Files Explanation

data_collection.py: This script will fetch 300 users of CNNBreakingNews to create training data. User who has more than 30 tweets and more than 10 followers will be labeled as active user. On the other hand, the rest of the users would be labeled as inactive users. Both category would be saved as json in data folder. Since twitter api only allow you to query 300 users every 15 minutes, I fetched 300 users for training set because that's enough. You can also fetch more by comment out this line:

    if len(follower_list) >= 300:
        break
fetch_test_data.py: This script fetch 50 users's information for test.
stream.py: You can also use this script to test. Since it can only fetch 300 users each 15 minutes, you need to use fetch_test_data.py if you want to test more.
test.py:Use this script to train and test.(I strongly recommend you to use this script instead of stream.py)

Wekinator Configuration

2 inputs(number of tweets and number of followers of a user), 1 output(classifiers with 2 classes) I used Processing_TriggerText_1Classifier from the example bundle.

Train your model

Select class 1 in wekinator output.
Run test.py using the following command:
    python test.py --file active
Start recording in wekinator. (10-15 example are strongly recommended for a higher accuracy.)
Stop recording and stop the script.
Select class 2 in wekinator output.
Run test.py using the following command:
    python test.py --file inactive
Start recording in wekinator. (10-15 example are strongly recommended for a higher accuracy.)
Stop recording and stop the script.
Train your model in wekinator
Run to test

Click run in wekinator
Run test.py using the following command:
    python test.py --file test
You will see inactive user is identified as blue in output program ans active user is red. And you can see the actual stats of each user when running this script.

That's it!