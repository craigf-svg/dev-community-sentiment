# Labels: 0 -> Negative; 1 -> Neutral; 2 -> Positive
label_rank = {
    'LABEL_0': 0,
    'LABEL_1': 1,
    'LABEL_2': 2
}
# For sentiment analysis, we find the average of these values for our formula:
SENTIMENT_SCORES = {
        'LABEL_0': -1,
        'LABEL_1': 0,
        'LABEL_2': +1
    }
label_text = {
    0: 'Negative',
    1: 'Neutral',
    2: 'Positive'
}

# Function that restructures a single post into a standardized format
def restructure_single_post(post):
    sentiment_label = post['sentiment'][0]['label']
    label_number = label_rank[sentiment_label]
    mood = label_text[label_number]
    sentiment_score = post['sentiment'][0]['score']
    return {
        'post_title': post['title'],
        'label': sentiment_label,
        'label_rank': label_rank[sentiment_label],
        'mood': mood,
        'score': sentiment_score,
    }

# Function to restructure posts by subreddit
def restructure_subreddits_posts(results, subreddit, posts):
    for post in posts:
        if subreddit in results:
            results[subreddit].append(restructure_single_post(post))
        else:
            results[subreddit] = [restructure_single_post(post)]
    print(results)

# Function to structure the sentiment data by subreddit
def structure_sentiment_data(data):
    result = {}
    for subreddit, posts in data.items():
        restructure_subreddits_posts(result, subreddit, posts)
    return result

# Function to calculate the average sentiment score of posts
def calculate_average_sentiment(post_list):
    # Positive = +1, Neutral = 0, Negative = -1
    print('posts_list', post_list)
    for post in post_list:
        sentiment_label = post['label']
        post['score'] = SENTIMENT_SCORES[sentiment_label]
    # Calculate the average sentiment score
    total_score = sum(post['score'] for post in post_list)
    average_score = round(total_score / len(post_list), 2)
    return average_score

# Function to sort subreddits by average sentiment
def sort_by_sentiment(posts):
    subreddit_sentiments = structure_sentiment_data(posts)
    aggregated = {}
    # For each list of posts sorted by subreddit
    for subreddit, post_list in subreddit_sentiments.items():
        if not post_list:
            continue
        top_post = max(post_list, key=lambda x: x['score'])
        average_score = calculate_average_sentiment(post_list)
        aggregated[subreddit] = {
            'top_post': top_post['post_title'],
            'label_rank': top_post['label_rank'],
            'score': top_post['score'],
            'average_score': average_score,
            'all_posts': post_list
        }

    sorted_subreddits = dict(sorted(
        aggregated.items(),
        key=lambda x: (x[1]['average_score']),
        reverse=True
    ))
    return sorted_subreddits