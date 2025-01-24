import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from matplotlib.dates import DateFormatter

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TrendVisualizer:
    def __init__(self, data_file, output_dir='visualizations'):
        self.data_file = data_file
        self.output_dir = output_dir
        sns.set_theme(style='darkgrid')
    
    def load_data(self):
        """Load trend data from CSV file."""
        logging.info("Loading data from file...")
        df = pd.read_csv(self.data_file, parse_dates=['date'], index_col='date')
        df.fillna(0, inplace=True)
        return df

    def plot_trend_over_time(self, df):
        """Generate a trend over time visualization."""
        plt.figure(figsize=(12, 6))
        for column in df.columns:
            plt.plot(df.index, df[column], label=column)
        plt.title('Google Trends Data Over Time')
        plt.xlabel('Date')
        plt.ylabel('Search Interest')
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.savefig(f'{self.output_dir}/trend_over_time.png')
        logging.info("Trend over time visualization saved.")

    def plot_heatmap(self, df):
        """Generate a heatmap visualization."""
        plt.figure(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Keyword Correlation Heatmap')
        plt.savefig(f'{self.output_dir}/correlation_heatmap.png')
        logging.info("Correlation heatmap saved.")

    def plot_moving_average(self, df, window=7):
        """Plot moving averages for each keyword."""
        plt.figure(figsize=(12, 6))
        for column in df.columns:
            df[column].rolling(window=window).mean().plot(label=f'{column} {window}-day MA')
        plt.title(f'Moving Average ({window}-Day) of Search Trends')
        plt.xlabel('Date')
        plt.ylabel('Search Interest')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'{self.output_dir}/moving_average.png')
        logging.info("Moving average visualization saved.")

    def run_visualizations(self):
        df = self.load_data()
        self.plot_trend_over_time(df)
        self.plot_heatmap(df)
        self.plot_moving_average(df)
        logging.info("All visualizations completed.")

if __name__ == "__main__":
    visualizer = TrendVisualizer(data_file='google_trends_data.csv')
    visualizer.run_visualizations()
