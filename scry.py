import os
import praw
from transformers import pipeline
from dotenv import load_dotenv
from utils import test_reddit_connection

load_dotenv()

# Load CardiffNLP sentiment analysis model from the Hugging Face Transformers library
classifier = pipeline("sentiment-analysis",
                      model="cardiffnlp/twitter-roberta-base-sentiment")

reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     user_agent=os.getenv("USER_AGENT"))


def invoke_scry(subreddit):
    # Fetches top posts from forum and returns with title of post + sentiment analysis of post title
    subreddit = reddit.subreddit(subreddit)
    top_posts = subreddit.top(time_filter='day', limit=8)
    posts = []
    
    print(f"Gathering posts from subreddit: {subreddit.display_name}")
    for post in top_posts:
        max_posts = 5
        if not post.stickied:
            sentiment = classifier(post.title)
            sentiment[0]['score'] = round(sentiment[0]['score'], 2)
            posts.append({'title': post.title, 'sentiment': sentiment})
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
