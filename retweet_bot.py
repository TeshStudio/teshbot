# Import Tweepy, sleep, credentials.py
import tweepy
import random
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

current_follow = 0;
Max_Follow = 5;

word_choice = ['Some cool stuff!', 'Check this out!', 'More great stuff!', 'Take a look at tthis!']

tag = str(raw_input("Input hashtag without # >> "))
dofollow = str(raw_input("yes for follow and no For dont follow >> "))
dofavorite = str(raw_input("yes for favorite and no for dont favorite >> "))
typepost = str(raw_input("retweet for retweet and quote for quote >> "))
sleeptime = int(raw_input("How long do you wan't the bot to sleep in between >> "))

def begin():
    
    for tweet in tweepy.Cursor(api.search, q='#' + tag).items():
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
            global current_follow
            current_follow += 1;
            print('\nCurrent Folllow Index: ' + str(current_follow))

            if not tweet.user.screen_name == 'TeshBroAds':
                if typepost == 'retweet':
                    tweet.retweet()
                    print('Retweeted the tweet')
                if typepost == 'quote':    
                    api.update_status(random.choice(word_choice) + ' @' + tweet.user.screen_name + ' https://twitter.com/' + tweet.user.screen_name + '/status/' + tweet.id_str)
                    print('quoted the tweet')

            if not tweet.user.screen_name == 'TeshBroAds':
                if dofavorite == 'yes':
                    # Favorite the tweet
                    tweet.favorite()
                    print('Favorited the tweet')
                else:
                    print('Didnt Favorite')

            if not tweet.user.following:
                if current_follow >= Max_Follow and dofollow == 'yes': 
                    # Don't forget to indent
                    current_follow = 0;
                    tweet.user.follow()
                    print('Followed the user')
                else:
                    print('not followed')

            sleep(5)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
        sleep(sleeptime)

begin()
