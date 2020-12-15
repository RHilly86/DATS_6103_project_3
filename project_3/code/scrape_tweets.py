import pandas as pd
import pickle
from tqdm import tqdm
import time
import tweepy
import os
os.chdir("/Users/rhilly/Desktop/DATS_6103/project_3/code")
import config

auth = tweepy.OAuthHandler(config.api_key, config.secret_key)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

search_query = "@timnitGebru OR Timnit Gebru OR timnit gebru OR #ISupportTimnit OR (@timnitGebru AND #BelieveBlackWomen) OR (Timnit Gebru AND #BelieveBlackWomen) OR (timnit gebru AND #BelieveBlackWomen) AND exclude:retweets"

def scrape_tweets(runs, search_terms, since_date):
    
    # Assign None to lowest_id as there won't be IDs on the first request to the Twitter API
    lowest_id = None
    tweets = []
    ids = []
    
    for i in range(runs):
        print(f"Starting run #{i + 1}")
        
        try:
            # Iteratively scrape batches of tweets and append the tweets and the IDs of
            # the tweets to the appropriate lists
            for tweet in tqdm(tweepy.Cursor(api.search, q=search_terms,
                                           since=since_date, max_id=lowest_id,
                                           tweet_mode="extended",
                                           lang="en").items()):
                tweets.append(tweet)
                ids.append(tweet.id)
        
        # We'll eventually hit a rate limit (~2500 - 2700 tweets) so we'll handle this error 
        except tweepy.TweepError:
            
            # If we've finished the last run, return the tweets that were scraped
            if (i + 1) == runs:
                print(f"Scraping complete. You collected {len(tweets)} tweets in {runs} runs. \n Dumping tweets to a text file using pickle...")
                with open("/Users/rhilly/Desktop/DATS_6103/project_3/data/timnit_tweets.txt", "wb") as f:
                    pickle.dump(tweets, f)
                break
            
            # Get the tweet with the smallest ID and use this in the next run
            lowest_id = min(ids)
            print(f"Finished run #{i + 1}. Sleeping for 20 minutes...")
            time.sleep(1200)
            
            
if __name__ == "__main__":
    scrape_tweets(4, search_query, "2020-12-2")
