from db_insert_posts import insert_post_list
from fetch_logger import log_fetch_result
from restructure_data import structure_sentiment_data, calculate_average_sentiment, average_sentiment_label


def process_and_insert(posts_data):
    # Structure Data
    subreddit_sentiments = structure_sentiment_data(posts_data)
    aggregated = {}
    total_success_count = 0
    total_skipped_count = 0
    # Loop+insert newly structured data by post list of each subreddit
    for subreddit, post_list in subreddit_sentiments.items():
        if not post_list:
            continue

        successfully_inserted_count, not_inserted_count = insert_post_list(
            post_list)
        total_success_count += successfully_inserted_count
        total_skipped_count += not_inserted_count

        average_score = calculate_average_sentiment(post_list)
        aggregated[subreddit] = {
            'average_score': average_score,
            'average_sentiment_label': average_sentiment_label(average_score)
        }

    log_fetch_result(post_list, total_success_count, total_skipped_count)
    sorted_subreddits = dict(sorted(
        aggregated.items(),
        key=lambda x: x[1]['average_score'],
        reverse=True
    ))

    return sorted_subreddits
