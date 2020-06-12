#!/usr/bin/env python3
import tweepy

import time
import os

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

def main():
    search = ("") #use a tag or an @ mention for what your bot is going to retweet

    numberofTweets = 50 #enter the number of retweets your bot will preform (100 is pushing the boundaries of twitter)
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.retweet()
            print("") #enter some message here for you so you know your bot is running
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
            time.sleep(1800) #amount of time before the next retweet
main()
