<a class="copyrighted-badge" title="Copyrighted.com Registered &amp; Protected" target="_blank" href="https://www.copyrighted.com/work/SDN9EdkW1uqttNJe"><img alt="Copyrighted.com Registered &amp; Protected" border="0" width="125" height="25" srcset="https://static.copyrighted.com/badges/125x25/03_1_2x.png 2x" src="https://static.copyrighted.com/badges/125x25/03_1.png" />
# Retweet Bot

Retweet Bots are scripts that search Twitter for tweets that mention a certain word or phrase, in my case a hashtag or a @mention of a user, and then can automatically retweet them.

## Python Library

Use the package manager [pip3](https://pypi.org/project/tweepy/) to install Tweepy.

```bash
pip3 install tweepy
```

## Code Snippet

```
import tweepy # Logging can be disabled and the 25 retweet limit as well
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
```

## Copyright

Retweet bot has been filed alongside Momentary Bot under the same copyright as they have the same codebase

Momentary Bot is copyrighted by the Twitter user @60MilesPerHour, Momentary Bot is copyrighted (c) under copyrighted.com

I hereby grant you the downloader of my program to use this software free of charge. I the creator of this software grant you permission to use the mentioned software without restriction, however, you are hereby subject to the following conditions

- The software you download is provided as is without any such warranty of any kind. 

- You are forbidden to merchandise off of this software unless otherwise granted by me, the author of this software.

By downloading this software, you agree that i the issuer am not liable for any infringement, claims, damages, or any other liabilities, whether contracted or otherwise.

Contact @60MilesPerHour if you have any questions and i will try to answer them to the best of my ability.
