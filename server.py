from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from scry import gather_conclave
from sentiment_analysis import sort_by_sentiment
from sample_data import sample_posts, sample_sorted_subs
from datetime import datetime, timedelta
from subreddit_groups import subreddit_groups
import os
from dotenv import load_dotenv
from models import db, SubredditSentiment
from config import Config
from datetime import date
from utils import subreddit_emojis

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    filter_date = date(2025, 4, 14)
    results = SubredditSentiment.query.filter_by(date=filter_date).limit(10).all()
    if results:
        return render_template('leaderboard.html', leaderboard=results)
    else:
        return "No data available"


@app.route('/test_db', methods=['GET', 'POST'])
def test_db():
    results = SubredditSentiment.query.limit(10).all()
    results_to_print = []
    if results:
        for entry in results:
            results_to_print +=[f"Subreddit: {entry.subreddit}, Date: {entry.date}, Avg Sentiment: {entry.avg_sentiment}"]
    else:
        results_to_print = "No data available"

    return f"First 10 subreddit sentiments:\n{results_to_print}"


def get_last_update():
    # Sample Function
    return "2025-04-15 08:30:00"


@app.route('/')
def home():
    # Calculate sample time remaining until next update
    last_update = get_last_update()
    last_update_datetime = datetime.strptime(last_update, "%Y-%m-%d %H:%M:%S")
    next_update = last_update_datetime + timedelta(days=1)
    time_remaining = next_update - datetime.now()
    return render_template('index.html', last_update=last_update, time_remaining=time_remaining)


@app.route('/scry', methods=['GET', 'POST'])
def scry():
    # Fetch + analyze subreddit sentiment
    subreddits = subreddit_groups

    posts = gather_conclave(subreddits)

    if posts:
        subreddit_titles_sorted = sort_by_sentiment(posts)
    else:
        subreddit_titles_sorted = sort_by_sentiment(sample_posts)
        posts = sample_posts

    return render_template('scry.html', sorted_subreddits=subreddit_titles_sorted, posts=posts, subreddit_emojis=subreddit_emojis)


if __name__ == '__main__':
    app.run(debug=True)
