import tweepy
import time
print('This is my bot')


CONSUMER_KEY = 'QgTjPyVRF5HDk2Xj4navjBzU7'
CONSUMER_SECRET = '577Fh74xA5XRPCQtiZJ03q0qQUjqJMzMjJaNRvATF6XAHOMcUK'
ACCESS_KEY = '1105871214600323072-9614fhlvtpSUKK0XiSzBPwrZa8YSRe'
ACCESS_SECRET = 'B1MPtfIij6HFizjAIrj7xNqJrYcSUmCsyGu6HJFW4hm5l'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...')


    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                    last_seen_id,
                    tweet_mode = 'extended')
    for mention in reversed(mentions):
        print(str(mention.id) + '-' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#HelloWorld' in mention.full_text.lower():
            print('found tweets...')
            print('responding_back!')
            api.update_status('@' + mention.user.screen_name + ' Thanks for tweet!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
