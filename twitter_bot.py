import tweepy
import time




# these are the key to acces your twitter
CONSUMER_KEY = 'xxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxx'
ACCESS_KEY = 'xxxxxxxx'
ACCESS_SECRET = 'xxxxxxx'

# Authentication set-ups
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# initializing FILE_NAME with last seen id
FILE_NAME = 'last_seen_id.txt'

print('This is my bot')

# getting last seen id
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

# storing last seen id to avoid overriding
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# reply to tweets if found #helloworld
def reply_to_tweets():
    print('retrieving tweets...')


    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                    last_seen_id,
                    tweet_mode = 'extended')
    for mention in reversed(mentions):
        print(str(mention.id) + '-' + mention.full_text)
        text = mention.full_text
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloWorld' in text.lower():
            print('found tweets...')
            print('responding_back!')
            api.update_status('@' + mention.user.screen_name + ' Thanks for tweet!', mention.id)

while True:
    reply_to_tweets()
    # reply and sleep for 15sec
    time.sleep(15)
