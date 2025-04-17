import prawcore
import praw

# Labels: 0 -> Negative; 1 -> Neutral; 2 -> Positive
label_rank = {
    'LABEL_0': 0,
    'LABEL_1': 1,
    'LABEL_2': 2
}
label_text = {
    0: 'Negative',
    1: 'Neutral',
    2: 'Positive'
}

# TODO: If two subreddits have the same sentiment label, sort by sentiment score


def structure_sentiment_data(data):
    # Returns
    result = {}
    for subreddit, posts in data.items():
        # Extract the sentiment label from the first post's sentiment
        sentiment_label = posts[0]['sentiment'][0]['label']
        label_number = label_rank[sentiment_label]
        mood = label_text[label_number]
        sentiment_score = posts[0]['sentiment'][0]['score']
        result[subreddit] = {
            'post_title': posts[0]['title'],
            'label': sentiment_label,
            'label_rank': label_rank[sentiment_label],
            'mood': mood,
            'score': sentiment_score,
        }
    return result


def sort_by_sentiment(posts):
    subreddit_sentiments = structure_sentiment_data(posts)
    # Subreddit title key -> sentiment label + score
    sorted_subreddits = dict(sorted(
        subreddit_sentiments.items(),
        key=lambda x: (
            x[1]['label_rank'], x[1]['score']),
        reverse=True
    ))
    return sorted_subreddits


def test_reddit_connection(reddit):
    # Attempt to fetch posts from r/technology subreddit as a test
    # This will raise an exception if the connection fails
    try:
        subreddit = reddit.subreddit('technology')
        list(subreddit.top(limit=2))

        print("Reddit connection successful.")
        return True

    except (praw.exceptions.RedditAPIException, praw.exceptions.ClientException) as e:
        print(f"Reddit API Error: {e}")
    except prawcore.exceptions.PrawcoreException as e:
        print(
            f"Reddit authentication error in test_reddit_connection: {e}.\n\nCheck your PRAW credentials and restart server or terminal if needed.")
    except Exception as e:
        print(f"An error occurred in test_reddit_connection: {e}")

    return False
