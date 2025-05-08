from flask import Flask, render_template
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from scry import gather_conclave
from sentiment_analysis import sort_by_sentiment
from sample_data import sample_posts, sample_sorted_subs
from datetime import datetime, timedelta
from subreddit_groups import subreddit_groups
import os
from dotenv import load_dotenv
from models import db, Post
from config import Config
from datetime import date
from utils import subreddit_emojis
import json

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route('/all_time_leaderboard', methods=['GET', 'POST'])
def all_time_leaderboard():
    results = (
        db.session.query(
            Post.subreddit,
            func.round(func.avg(Post.sentiment_score),
                       2).label("avg_sentiment")
        )
        .group_by(Post.subreddit)
        .order_by(func.avg(Post.sentiment_score).desc())
        .all()
    )
    return render_template('all_time_leaderboard.html', leaderboard=results, subreddit_emojis=subreddit_emojis)


@app.route('/daily_leaderboard', methods=['GET', 'POST'])
def daily_leaderboard():
    filter_date = date(2025, 5, 3)
    results = (
        db.session.query(
            Post.subreddit,
            func.round(func.avg(Post.sentiment_score),
                       2).label("avg_sentiment")
        )
        .filter(Post.post_date_est == filter_date)
        .group_by(Post.subreddit)
        .order_by(func.avg(Post.sentiment_score).desc())
        .all()
    )
    # all keys: post_id, subreddit, timestamp_utc, post_date_utc, post_date_est, sentiment_label:Neutral, sentiment_score:0, model_label:LABEL_1, model_confidence:0.82
    if results:
        return render_template('daily_leaderboard.html', leaderboard=results, subreddit_emojis=subreddit_emojis)
    else:
        return "No data available"


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
