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
# For sentiment analysis, we find the average of these values for our formula:
SENTIMENT_SCORES = {
    'LABEL_0': -1,
    'LABEL_1': 0,
    'LABEL_2': +1
}


def average_sentiment_label(score):
    if score <= -0.1:
        return 'Negative'
    elif score > -0.1 and score < 0.1:
        return 'Neutral'
    else:
        return 'Positive'


def restructure_single_post(post):
    sentiment_label = post['sentiment'][0]['label']
    label_number = label_rank[sentiment_label]
    mood = label_text[label_number]
    sentiment_score = post['sentiment'][0]['score']
    return {
        'post_title': post['title'],
        'subreddit': post['subreddit'],
        'label': sentiment_label,
        'label_rank': label_rank[sentiment_label],
        'mood': mood,
        'score': sentiment_score,
        'post_id': post['post_id'],
        'timestamp_utc': post['timestamp_utc']
    }


def restructure_subreddits_posts(results, subreddit, posts):
    for post in posts:
        if subreddit in results:
            results[subreddit].append(restructure_single_post(post))
        else:
            results[subreddit] = [restructure_single_post(post)]
    print(results)


def structure_sentiment_data(data):
    result = {}
    for subreddit, posts in data.items():
        restructure_subreddits_posts(result, subreddit, posts)
    return result


def calculate_average_sentiment(post_list):
    print('posts_list', post_list)
    for post in post_list:
        sentiment_label = post['label']
        post['score'] = SENTIMENT_SCORES[sentiment_label]
    total_score = sum(post['score'] for post in post_list)
    average_score = round(total_score / len(post_list), 2)
    return average_score
