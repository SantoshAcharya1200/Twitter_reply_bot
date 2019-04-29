import tweepy as tp
import time
import os
import random

print('this is my twitter bot', flush=True)

# credentials to login to twitter api
consumer_key = 'oaRIwSuor3TkRHJugpEVcEYGc'
consumer_secret = 'yIBgIKiyBKmmdTP7hg7oGqp5z5IZAUQDa2vya8uWMnOTBnsXBM'
access_token = '1110844547972526081-aFlW7SodvRyaOLgKTWt4sOgizUyElO'
access_secret = 'BSSKflPR7iGqpWMd6g23sYU3KEbOfhRbRIZVZgnaEVlvI'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

FILE_NAME = 'last_seen_id.txt'
print(os.getcwd())



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
    print('retrieving and replying to tweets...', flush=True)

    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if '#inspirationalquote' in mention.full_text.lower():
            print('found #inspirationalquote!', flush=True)
            print('responding back...', flush=True)
            sn = mention.user.screen_name
            stat = "@" + sn + " Have a nice day "
            os.chdir('C:\\Users\\santosh\\PycharmProjects\\first_project\\quotes')
            model_image = random.choice(os.listdir('.'))      #C:\Users\santosh\PycharmProjects\first_project\quotes
            api.update_with_media(model_image, stat, mention.id)


while True:
    reply_to_tweets()
    time.sleep(15)


