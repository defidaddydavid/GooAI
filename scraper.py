import requests
import pandas as pd
from pytrends.request import TrendReq
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GoogleTrendsScraper:
    def __init__(self, keywords, timeframe='today 3-m', geo='', category=0, retries=3, delay=5):
        self.keywords = keywords
        self.timeframe = timeframe
        self.geo = geo
        self.category = category
        self.retries = retries
        self.delay = delay
        self.pytrends = TrendReq(hl='en-US', tz=360)

    def fetch_trends(self):
        logging.info("Fetching Google Trends data...")
        trend_data = pd.DataFrame()
        
        for keyword in self.keywords:
            for attempt in range(self.retries):
                try:
                    logging.info(f"Fetching data for keyword: {keyword}")
                    self.pytrends.build_payload([keyword], cat=self.category, timeframe=self.timeframe, geo=self.geo)
                    data = self.pytrends.interest_over_time()
                    if not data.empty:
                        data.drop(columns=['isPartial'], inplace=True)
                        data['keyword'] = keyword
                        trend_data = pd.concat([trend_data, data])
                    break
                except requests.exceptions.RequestException as e:
                    logging.error(f"Request failed: {e}. Retrying in {self.delay} seconds...")
                    time.sleep(self.delay)
        
        logging.info("Data fetching completed.")
        return trend_data

    def save_to_csv(self, df, filename='google_trends_data.csv'):
        if not df.empty:
            df.to_csv(filename, index=True)
            logging.info(f"Data saved to {filename}")
        else:
            logging.warning("No data to save.")

    def run(self):
        data = self.fetch_trends()
        self.save_to_csv(data)
        return data

if __name__ == "__main__":
    keywords = ["Bitcoin", "Ethereum", "AI technology", "NFTs", "Solana"]
    scraper = GoogleTrendsScraper(keywords, timeframe='now 7-d')
    trends_data = scraper.run()
    print(trends_data.head())
