from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import time
import twitter_credentials

AUTH = OAuthHandler(twitter_credentials.CONSUMER_TOKEN, twitter_credentials.CONSUMER_SECRET)
AUTH.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)  

class TwitterStreamer():
    #Class to stream and process tweets of Donald Trump
    
    def stream_tweets(self, filename):
        #handles authentication and connection with Twitter API

        listener = StdOutListener(filename, time_limit=20) 

        #create stream and filter to user @realDonaldTrump
        stream = Stream(AUTH, listener)
        stream.filter(follow=["25073877"], is_async=True)

    def post_tweets(self):
        twitterApi = API(AUTH)
        api.update_status("Test Tweet")
        

class StdOutListener(StreamListener):
    #class to process received tweets
    def __init__(self, filename, time_limit=60):
       self.filename = filename
       self.start_time = time.time()
       self.limit = time_limit


    def on_data(self, data):
        try:
            tf = open(filename, 'a')
            if(time.time() - self.start_time) < self.limit:
                tf.write(data)
                return True
            else:
                tf.close()
                return False
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)

class JsonParser(self):
    
    def
if __name__ == "__main__":

    filename  = "tweets.json"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(filename)
    #twitter_streamer.post_tweets()
    
    
    
    

   
   

