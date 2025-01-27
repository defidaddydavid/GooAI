import pandas as pd
import re
import logging
from textblob import TextBlob
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SentimentAnalyzer:
    def __init__(self, data_file, use_advanced_model=True):
        self.data_file = data_file
        self.use_advanced_model = use_advanced_model
        self.sentiment_pipeline = pipeline('sentiment-analysis') if use_advanced_model else None
    
    def preprocess_text(self, text):
        """Clean text by removing special characters, links, and extra spaces."""
        text = re.sub(r'http\S+|www\S+', '', text)
        text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
        text = text.lower().strip()
        return text
    
    def analyze_sentiment(self, text):
        """Analyze sentiment using either TextBlob or Hugging Face model."""
        text = self.preprocess_text(text)
        if self.use_advanced_model:
            result = self.sentiment_pipeline(text)[0]
            sentiment_score = result['score'] if result['label'] == 'POSITIVE' else -result['score']
        else:
            sentiment_score = TextBlob(text).sentiment.polarity
        return sentiment_score
    
    def process_data(self):
        """Load data, analyze sentiment, and save results."""
        logging.info("Loading data...")
        df = pd.read_csv(self.data_file)
        df.dropna(subset=['keyword'], inplace=True)
        logging.info("Analyzing sentiment...")
        df['sentiment_score'] = df['keyword'].apply(self.analyze_sentiment)
        df['sentiment_category'] = df['sentiment_score'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
        output_file = 'analyzed_sentiment.csv'
        df.to_csv(output_file, index=False)
        logging.info(f"Sentiment analysis completed. Results saved to {output_file}")
        return df

if __name__ == "__main__":
    analyzer = SentimentAnalyzer(data_file='google_trends_data.csv', use_advanced_model=True)
    analyzed_data = analyzer.process_data()
    print(analyzed_data.head())
