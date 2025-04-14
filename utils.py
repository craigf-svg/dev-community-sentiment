import prawcore
import praw

# Labels: 0 -> Negative; 1 -> Neutral; 2 -> Positive
label_order = {
    'LABEL_0': 0,
    'LABEL_1': 1,
    'LABEL_2': 2
}

# TODO: If two subreddits have the same sentiment label, sort by sentiment score


def restructure_sentiment_data(data):
    result = {}
    print('data', data)
    for subreddit, posts in data.items():
        # Extract the sentiment label from the first post's sentiment
        sentiment_label = posts[0]['sentiment'][0]['label']
        result[subreddit] = sentiment_label
    return result


def sort_by_sentiment(posts):
    newData = restructure_sentiment_data(posts)
    sortedData = sorted(
        newData, key=lambda x: label_order[newData[x]], reverse=True)
    return sortedData


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
