from flask import Flask, render_template
from scry import gather_conclave
from utils import sort_by_sentiment
from sample_data import sample_posts, sample_sorted_subs

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/scry')
def scry():
    # Fetch + analyze subreddit sentiment
    subreddits = ["python", "learnprogramming", "flask"]

    posts = gather_conclave(subreddits)

    # Use sample data on exception
    if posts:
        sorted_subreddits = sort_by_sentiment(posts)
    else:
        sorted_subreddits = sample_sorted_subs
        posts = sample_posts

    return render_template('scry.html', sorted_subreddits=sorted_subreddits, posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
