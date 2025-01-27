import tweepy
import os
import pandas as pd
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TwitterBot:
    def __init__(self):
        self.api = self.authenticate()
        self.trend_data_file = 'data/trends_sentiment.csv'
    
    def authenticate(self):
        """Authenticate with the Twitter API using environment variables."""
        logging.info("Authenticating with Twitter API...")
        auth = tweepy.OAuthHandler(os.getenv('TWITTER_CONSUMER_KEY'), os.getenv('TWITTER_CONSUMER_SECRET'))
        auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_SECRET'))
        return tweepy.API(auth, wait_on_rate_limit=True)
    
    def load_trends(self):
        """Load trends and sentiment data from CSV."""
        logging.info("Loading trend data...")
        df = pd.read_csv(self.trend_data_file)
        df.dropna(subset=['keyword', 'sentiment_category'], inplace=True)
        return df
    
    def generate_tweet(self, df):
        """Generate an engaging tweet from the latest trend data."""
        top_trend = df.sort_values(by=['sentiment_score'], ascending=False).iloc[0]
        keyword = top_trend['keyword']
        sentiment = top_trend['sentiment_category']
        trend_score = top_trend['sentiment_score']

        tweet_text = (
            f"Trending Now: {keyword}\n"
            f"Sentiment: {sentiment}\n"
            f"Interest Score: {trend_score:.2f}\n"
            f"Stay updated with #GooAI."
        )
        logging.info(f"Generated tweet: {tweet_text}")
        return tweet_text
    
    def post_tweet(self):
        """Post the generated tweet to Twitter."""
        df = self.load_trends()
        tweet_content = self.generate_tweet(df)
        try:
            self.api.update_status(tweet_content)
            logging.info("Tweet posted successfully.")
        except tweepy.TweepError as e:
            logging.error(f"Failed to post tweet: {e}")

    def schedule_tweets(self, interval_hours=6):
        """Schedule tweets to post at regular intervals."""
        from time import sleep
        while True:
            self.post_tweet()
            logging.info(f"Next tweet scheduled in {interval_hours} hours.")
            sleep(interval_hours * 3600)

if __name__ == "__main__":
    bot = TwitterBot()
    bot.post_tweet()
