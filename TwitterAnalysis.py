
# coding: utf-8

# In[4]:

sc


# In[5]:

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql import functions as F
import os
import re
import tweepy


# In[6]:

print(os.listdir())
ssc = StreamingContext(sc, 10 )
sqlContext = SQLContext(sc)
ssc.checkpoint(str(os.path)+"/checkpoint")


# In[7]:

ip = get_ipython().magic('system ifconfig')


# In[10]:

ipAdd = list(filter(lambda x: "inet addr:192" in x,ip))
extracted = re.search(r"inet addr:\d{3}\.\d{3}\.\d{1,3}\.\d{1,3}",ipAdd[0])


# In[9]:

adress = re.search(r'\d+\.\d+\.\d+\.\d+', extracted.group(0))
ipAddress = [int(i) for i in adress.group(0).split(".")]
print(ipAddress)


# In[11]:



#Variables that contains the user credentials to access Twitter API 
consumer_key = 'B8hcPElr1sX7QnC4FzuxQZ3mw'
consumer_secret = '4CzdOFZrwOY4M6oMx3KxaBSuabpADq8o90PhRznBzlQCczJ3tU'
access_token = '742610974516072448-4vKn9jwMpGN6wFla8ZBVeR2Fsv6Pmm8'
access_token_secret = 'HwoAUGEN1xageZ0x9uPyFEpXHDRUsfFjw0sPyQTfKtJEl'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#show my own tweets from my time line
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


# In[12]:

user = api.get_user('baumRn')


# In[13]:

for v in user.timeline():
    #print(v)

    print(str(v.id)+"\t"+v.text+"\t"+str(v.created_at))
    print("\n")


# In[14]:

#people following Thorbjørn

for i in user.followers():
    print(i.name)
    
tbTimeLine = user.timeline()


# In[23]:

#number of times Thorbjørn has been retweetedt
tbTimeLine


# In[ ]:



