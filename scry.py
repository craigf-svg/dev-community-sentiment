import os
import praw
from transformers import pipeline
from dotenv import load_dotenv
from utils import test_reddit_connection
from datetime import datetime
from zoneinfo import ZoneInfo

load_dotenv()

# Load CardiffNLP sentiment analysis model from the Hugging Face Transformers library
classifier = pipeline("sentiment-analysis",
                      model="cardiffnlp/twitter-roberta-base-sentiment")

reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     user_agent=os.getenv("USER_AGENT"))


def invoke_scry(subreddit):
    # To insert, current keys the posts have are 'post_title': When do you use threads, 'label': LABEL_1, 'label_rank': 1, 'mood': Neutral, 'score': 0.5
    # Fetches top posts from forum and returns with title of post + sentiment analysis of post title
    subreddit = reddit.subreddit(subreddit)
    top_posts = subreddit.top(time_filter='day', limit=8)
    today = datetime.today().date()
    posts = []
    print(f"Gathering posts from subreddit: {subreddit.display_name}")
    for post in top_posts:
        max_posts = 5
        if not post.stickied:
            # Experimenting with dates
            post_date = datetime.fromtimestamp(post.created, tz=ZoneInfo("UTC"))
            post_date_est = post_date.astimezone(ZoneInfo("America/New_York")).date()
            print('post_date', post_date, 'post_date_est', post_date_est)
            if today == post_date_est:
                sentiment = classifier(post.title)
                timestamp = post.created_utc
                subreddit = post.subreddit.display_name
                sentiment[0]['score'] = round(sentiment[0]['score'], 2)
                posts.append(
                    {'title': post.title, 'sentiment': sentiment, 'subreddit': subreddit, 'post_id': post.id, 'timestamp_utc': timestamp})
        if len(posts) >= max_posts:
            break

    return posts


def gather_conclave(subreddits):
    posts = {}
    if not test_reddit_connection(reddit):
        print("Reddit connection failed. Switching to sample data.")
        return False

    for subreddit in subreddits:
        posts[subreddit] = invoke_scry(subreddit)

    return posts
