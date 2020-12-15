import pandas as pd
import pickle
import re
import tweepy

def extract_attributes(tweets):
    tweet_attrs = []
    
    for tweet in tweets:
        created_at = tweet.created_at
        id = tweet.id
        tweet_text = tweet.full_text
        tweeter = tweet.user.screen_name
        tweeter_bio = tweet.user.description
        favs_on_tweet = tweet.favorite_count
        retweets_on_tweet = tweet.retweet_count
        tweeter_followers = tweet.user.followers_count
        
        tweet_attrs.append([created_at, id, tweet_text, tweeter,
                            tweeter_bio, favs_on_tweet, retweets_on_tweet,
                            tweeter_followers])
            
    return pd.DataFrame(tweet_attrs, columns=["created_at", "id", "tweet_text",
                                              "tweeter", "tweeter_bio", "favs_on_tweet",
                                              "retweets_on_tweet", "tweeter_followers"])

if __name__ == "__main__":
    with open("/Users/rhilly/Desktop/DATS_6103/project_3/data/timnit_tweets.txt", "rb") as f:
        timnit_tweets = pickle.load(f)
    
    timnit_tweets_tidy = extract_attributes(timnit_tweets)
    
    # Drop tweets from Tweetologist3
    # Filter out links in tweets (due to globalfirstnews)
    timnit_tweets_tidy = timnit_tweets_tidy[timnit_tweets_tidy["tweeter"] != "Tweetologist3"]
    timnit_tweets_tidy["tweet_text"] = timnit_tweets_tidy["tweet_text"].str.replace(r"https://t.co/\w*", "").str.strip()
    timnit_tweets_tidy.drop_duplicates(subset=["tweet_text"], inplace=True)
    
    timnit_tweets_tidy.to_csv("timnit_tweets_final.csv", index=False)
    
