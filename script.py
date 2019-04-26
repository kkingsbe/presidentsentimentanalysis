import tweepy
import textblob

def get_tweets():
    # Consumer keys and access tokens, used for OAuth
    consumer_token = '0OktKnQx37Rkpen4UElwgvU15'
    consumer_secret = 'VbGlGtbjLvpgfpKJ5LrvxmJkHNNneiZLl1frSkiCqj3qqwUsV6'
    access_token = '787287701934538752-w5r4YpcIVHgjBbwfzXvi645TPyIb2wQ'
    access_secret = 'ECx2U93WixPTF7hqC7JTH4x7XeyhQv96reFCVwvSaOmdJ'
    callback_url = "http://www.google.com"

    trump_tweets_file = open("Trump_Tweets.txt", "w+", encoding="utf-8")
    obama_tweets_file = open("Obama_Tweets.txt", "w+", encoding="utf-8")

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    for tweet in tweepy.Cursor(api.user_timeline, id='realDonaldTrump').items():
        print(tweet.text)
        trump_tweets_file.writelines(str(tweet.created_at) + " ; " + str(tweet.favorite_count) + " ; " + tweet.text.strip(" ; ").strip("\n") + "\n")

    for tweet in tweepy.Cursor(api.user_timeline, id='BarackObama').items():
        print(tweet.text)
        obama_tweets_file.writelines(str(tweet.created_at) + " ; " + str(tweet.favorite_count) + " ; " + tweet.text.strip(" ; ").strip("\n") + "\n")

    obama_tweets_file.close()
    trump_tweets_file.close()

def analyze_tweets():
    analysis_file = open("analysis.txt", "w+")

    trump_tweets = open("Trump_Tweets.txt", "r+", encoding="utf-8").readlines()
    obama_tweets = open("Obama_Tweets.txt", "r+", encoding="utf-8").readlines()

    for tweet in trump_tweets:
        if tweet != "\n":
            try:
                text = tweet.split(" ; ")[2]
                sentiment = textblob.TextBlob(text).sentiment.polarity
                print(text.strip() + " | " + str(sentiment))
                analysis_file.writelines(tweet.split(" ; ")[0] + " ; " + tweet.split(" ; ")[1] + " ; " + str(sentiment) + text)
            except:
                print("oopsies!")

#get_tweets()
analyze_tweets()