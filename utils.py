import prawcore
import praw

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
