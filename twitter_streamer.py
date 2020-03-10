from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

AUTH = OAuthHandler(twitter_credentials.CONSUMER_TOKEN, twitter_credentials.CONSUMER_SECRET)
AUTH.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)  

class TwitterStreamer():
    #Class to stream and process tweets of Donald Trump
    
    def stream_tweets(self, filename):
        #handles authentication and connection with Twitter API

        listener = StdOutListener(filename) 

        #create stream and filter to user @realDonaldTrump
        stream = Stream(AUTH, listener)
        stream.filter(follow=["25073877"], is_async=True)

    def post_tweets(self):
        twitterApi = API(AUTH)
        api.update_status("Test Tweet")
        

class StdOutListener(StreamListener):
    #class to process received tweets

    def __init__(self, filename):
       self.filename = filename
    def on_data(self, data):
        try:
            with open(self.filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":

    filename  = "tweets.txt"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(filename)
    #twitter_streamer.post_tweets()
    
    
    
    

   
   

