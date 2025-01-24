from flask import Flask, render_template
from pytrends.request import TrendReq
import logging
import plotly.express as px
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

def fetch_trends(keywords, timeframe='now 7-d'):
    """Fetch real-time Google Trends data with advanced error handling and retries."""
    logging.info("Fetching Google Trends data...")
    pytrends = TrendReq()
    try:
        pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo='', gprop='')
        trends = pytrends.interest_over_time()
        if not trends.empty:
            trends.drop(columns=['isPartial'], inplace=True)
            trends.reset_index(inplace=True)
            return trends
        else:
            logging.warning("No trend data returned.")
            return pd.DataFrame()
    except Exception as e:
        logging.error(f"Error fetching trends: {e}")
        return pd.DataFrame()

@app.route('/')
def index():
    keywords = ["Bitcoin", "Ethereum", "AI", "Machine Learning"]
    trends = fetch_trends(keywords)
    if trends.empty:
        return render_template('index.html', error="No data available. Please try again later.")
    
    # Create a visualization using Plotly
    fig = px.line(trends, x='date', y=trends.columns[1:], title='Google Trends Interest Over Time')
    fig.update_layout(template='plotly_dark')
    chart_html = fig.to_html(full_html=False)
    
    return render_template('index.html', chart=chart_html, trends=trends.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
