import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

def TwitterAuth():

    api_key = ["your_api_key"]
    api_secret = ["your_api_secret_key"]
    access_token = ["your_access_token"]
    access_token_secret = ["your_access_token_secret"]

    try:
        auth = OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    
    except:
        print("Error: Authentication Failed")

def get_tweets(api, query):
    public_tweets = api.search(query, count = 10)
    return public_tweets

def get_tweet_sentiment(tweets):
    for i, tweet in enumerate(tweets):
        print("Tweet #" + str(i + 1) + "\n" + tweet.text)
        analysis = TextBlob(tweet.text)
        
        if analysis.sentiment.polarity > 0:
            print("Positive")
        elif analysis.sentiment.polarity == 0:
            print("Neutral")
        else:
            print("Negative")

        print("\n\n")

def main():
    api = TwitterAuth()
    query = input("Enter query: ") # the query to be searched in twitter.
    tweets = get_tweets(api, query)
    get_tweet_sentiment(tweets)


if __name__ == "__main__":
    # calling main function
    main()
