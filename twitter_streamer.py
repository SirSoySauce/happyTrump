from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

class TwitterStreamer():
    #Class to stream and process tweets of Donald Trump

    def stream_tweets(self, filename):
        #handles authentication and connection with Twitter API

        listener = StdOutListener(filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_TOKEN, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

        #create stream and filter to user @realDonaldTrump
        stream = Stream(auth, listener)
        stream.filter(follow=["25073877"], is_async=True)

class StdOutListener(StreamListener):
    #class to process received tweets

    def __init__(self, filename):
       self.filename = filename
    def on_data(self, data):
        try:
            print(data)
            with open(self.filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":

    filename  = "tweets.json"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(filename)
    
    
    
    

   
   

