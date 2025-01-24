# GooAI
# GooAI

GooAI is an AI-powered Google Trends analysis tool that provides real-time insights into search trends and sentiment analysis across various topics. It is designed to help users track trends, visualize data, and automate reports for better decision-making.

## 🚀 Features

- **Real-Time Google Trends Data Fetching:** Leverages Google Trends API to fetch live data.
- **Sentiment Analysis:** Uses advanced NLP models to analyze search trends sentiment.
- **Interactive Data Visualization:** Provides trend graphs and insights via Plotly.
- **Automated Twitter Bot:** Posts trend updates directly to Twitter.
- **Web Dashboard:** Displays trend data in a user-friendly UI.
- **Scalable Deployment:** Optimized for cloud deployment via Render, AWS, or Heroku.

## 🛠️ Installation

### Prerequisites
Ensure you have the following installed:

- Python 3.9+
- Flask
- Pip
- Git

### Clone the Repository

```bash
git clone https://github.com/yourusername/GooAI.git
cd GooAI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the root directory and add:

```bash
FLASK_ENV=production
SECRET_KEY=your_secret_key
TWITTER_CONSUMER_KEY=your_key
TWITTER_CONSUMER_SECRET=your_secret
TWITTER_ACCESS_TOKEN=your_token
TWITTER_ACCESS_SECRET=your_secret
```

## 🚀 Usage

### Run the Application Locally

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

### Run with Gunicorn (Production Ready)

```bash
gunicorn app:app --workers 4 --bind 0.0.0.0:8000
```

## 🌐 Deployment

### Deploy on Render

1. Push your code to GitHub.
2. Create a new Render web service.
3. Set the build and start commands:
    - Build command: `pip install -r requirements.txt`
    - Start command: `gunicorn app:app`
4. Set environment variables in Render dashboard.
5. Deploy and access the app via Render-provided URL.

### Deploy on Heroku

```bash
heroku create gooai-app
heroku config:set SECRET_KEY=your_secret_key
heroku buildpacks:add heroku/python
git push heroku main
```

## 📊 Features Overview

### 1. Data Scraper
Fetches real-time Google Trends data with:

- Keyword-based data collection
- Timeframe customization
- Data cleansing and preprocessing

### 2. Sentiment Analysis
Uses machine learning models to analyze sentiment of trending search topics.

- TextBlob for basic analysis
- Hugging Face transformer models for advanced insights

### 3. Data Visualization
Provides interactive trend graphs, heatmaps, and moving averages.

- Powered by Matplotlib and Plotly

### 4. Twitter Bot Automation
Automatically posts daily trend reports to Twitter.

- Fully automated with Tweepy
- Scheduled posting supported

### 5. Web Dashboard
A clean and responsive UI to visualize trends with:

- Flask-based backend
- Bootstrap frontend with Plotly charts

## 📁 Project Structure

```
GooAI/
│-- templates/                 # HTML templates
│   ├── index.html
│-- static/                     # CSS, JS, images
│-- app.py                       # Flask web app backend
│-- requirements.txt              # Python dependencies
│-- .env                           # Environment variables
│-- README.md                      # Documentation
│-- Procfile                        # Deployment file for Heroku
│-- runtime.txt                     # Python version
```

## 🔍 API Endpoints

- **`GET /`** - Home page
- **`GET /trends`** - Fetches and displays trends data
- **`POST /analyze`** - Analyzes sentiment for given keywords

## 📋 Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.

## 🛡️ Security

If you discover a security vulnerability, please open an issue or reach out to the maintainers directly.

## 📜 License

This project is licensed under the MIT License.

## 🤝 Acknowledgments

Special thanks to contributors and the open-source community for inspiration and code contributions.

---

For more information, visit the [GooAI GitHub Repository](https://github.com/yourusername/GooAI).

---

