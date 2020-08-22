#This bot now also falls under Momentary Bot's copyright as they are based upon each others code

import tweepy # imports below are required (tweepy -> pip3 install tweepy)
import time
import os
import sys
#import time
import logging #required for logging functions (remove lines 8,9,11,13,14 and take out " + str(datetime.datetime.now()) from the lines below if not wanted")
import datetime 

x = datetime.datetime.now()

LOG_FILENAME = 'TwitterBotLogging.log' # will create this file if it doesn't already exist
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

consumer_key = '' #Lines 16 - 26 are required (you can take out the line that identify's your account if you want but i find it to be nice :)
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

def main():
    search = ("") #put in a @ symbol followed by the user example = @60MilesPerHour, can also be a # if your interested...

    numberofTweets = 25 #Must not exceed 25 but can be lower than 25 (able to be circumvented if you import sleep and time but i've found that twitter doesnt like that...)
    
    if numberofTweets <= 25:

        logging.debug('User Entered a # of: ' + numberofTweets + str(datetime.datetime.now()))

        for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
            try:
                tweet.retweet()
                print("") #enter some message here for you so you know your bot is running
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                # this is where you would put time.sleep(#of seconds to sleep)
                break
    else:
        logging.debug('User Entered a value above 25' + str(datetime.datetime.now()))
        sys.exit  #program will exit if numberofTweets = more than 25
main()
