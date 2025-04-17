from flask import Flask, render_template
from scry import gather_conclave
from utils import sort_by_sentiment
from sample_data import sample_posts, sample_sorted_subs
from datetime import datetime, timedelta

app = Flask(__name__)

# Sample Function
def get_last_update():
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
    subreddits = ['python', 'learnprogramming', 'flask']

    posts = gather_conclave(subreddits)

    if posts:
        subreddit_titles_sorted = sort_by_sentiment(posts)
    else:
        subreddit_titles_sorted = sort_by_sentiment(sample_posts)
        posts = sample_posts

    return render_template('scry.html', sorted_subreddits=subreddit_titles_sorted, posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
