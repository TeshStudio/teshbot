# Import our Twitter credentials from credentials.py
import tweepy
import io
from time import sleep
import sys
from credentials import *

#Access and authorize our twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

argfile = str(sys.argv[1])

# Open text file verne.txt (or your chosen file) for reading
my_file = open(argfile, 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

# Tweet a line every 15 minutes
def tweet():
    for line in file_lines:
        try:
             print(line)
             if line != '\n':
                 api.update_status(line)
                 sleep(60)
             else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(60)

tweet()
