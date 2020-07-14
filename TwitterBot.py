#this bot now also falls under Momentary Bot's copyright as they are based upon each others code

import tweepy #required
import time #required
import os #required
import sys #required

import logging #required for logging functions
import datetime #required for logging functions

x = datetime.datetime.now() #required for logging functions

LOG_FILENAME = 'TwitterBotLogging.log' #required for logging functions
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG) #required for logging functions

consumer_key = '' #required
consumer_secret = '' #required
access_token = '' #required
access_token_secret = '' #required

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #required
auth.set_access_token(access_token, access_token_secret) #required
api = tweepy.API(auth) #required

user = api.me() #required
print(user.name) #required

def main():
    search = ("") #put in a @ symbol followed by the user example = @60MilesPerHour

    numberofTweets = 25 #Must not exceed 25 but can be lower than 25
    
    if numberofTweets <= 25:

        logging.debug('User Entered a # of: ' + numberofTweets + str(datetime.datetime.now()))

        for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
            try:
                tweet.retweet()
                print("") #enter some message here for you so you know your bot is running
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
    else:
        logging.debug('User Entered a value above 25' + str(datetime.datetime.now()))
        sys.exit  #program will exit if numberofTweets = more than 25
main()
