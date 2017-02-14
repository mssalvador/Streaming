import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = 'B8hcPElr1sX7QnC4FzuxQZ3mw'
consumer_secret = '4CzdOFZrwOY4M6oMx3KxaBSuabpADq8o90PhRznBzlQCczJ3tU'
access_token = '742610974516072448-4vKn9jwMpGN6wFla8ZBVeR2Fsv6Pmm8'
access_token_secret = 'HwoAUGEN1xageZ0x9uPyFEpXHDRUsfFjw0sPyQTfKtJEl'



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['svanholm'])
