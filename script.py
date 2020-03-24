import re
import tweepy
import twitter_credentials


def get_word_dict_from_file(file):
    word_dict = {}
    lines = file.readlines()
    for line in lines:
        split_word = line.strip().split(':')
        word_dict[split_word[0]] = split_word[1]
    return word_dict


def replace_words_from_dict(dict, string):
    for word, initial in dict.items():
        string = re.sub('(?<=[?,!.:–"\\s#])' + word + '(?=[?,!.:–"\\s#])', initial, string, flags=re.IGNORECASE)
    return string


word_file = open('words.txt', 'r')
word_dict = get_word_dict_from_file(word_file)

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_TOKEN, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

f = open("latest_tweet_id.txt", "r")
latest_tweet_id = f.read()

timeline = api.user_timeline(user_id="25073877", since_id=latest_tweet_id, tweet_mode='extended')

for tweet in timeline:
    firstText = tweet.full_text
    editedText = replace_words_from_dict(word_dict, firstText)
    if firstText != editedText and len(editedText) <= 280 and editedText[:2] != 'RT':
        print(firstText)
        api.update_status(status=editedText)

if timeline.__len__() > 0:
    file_write = open("latest_tweet_id.txt", "w")
    file_write.write(timeline[0].id_str)
f.close()
