#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys

consumer_key='FxP0Di4XxFIUsjmmebzgYn9Wl'
consumer_secret='kCxga8v5DQ43ef9TVbJOD5prcv2zQc4VJobmsJo90W95z7u26c'
access_token='248651338-sKPGKaxmJq99n18pPFbGF5wZwacbz4hfz368ZOso'
access_token_secret='AToI9rCfHjEbrUIzULuy9aKywipvy1d15ZJWHAKmUiY4Q'

file1 = open('dataset.txt','w')

class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            
            jsonData = json.loads(data)
            text = jsonData['text'].lower()
            if "rt" in text:
                pass
            else:
                print(text+'\n')
                file1.write(text+'\n')
            return True

        except:
            return True
    def on_error(self, status):
         print (status)


if __name__ == '__main__':
    topic = sys.argv[1]
    print "Downloading Tweets on ", topic
    print "Press ctrl+c to stop downloading tweets."
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=[topic])
    
file1.close()
