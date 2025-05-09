from models import db, Post

SENTIMENT_SCORES = {
    'LABEL_0': -1,
    'LABEL_1': 0,
    'LABEL_2': +1
}


def insert_post_list(post_list):
    successfully_inserted_count = 0
    not_inserted_count = 0
    for post in post_list:
        try:
            # TODO: Make post_list follow format of ORM on creation
            # Rather than mapping here for consistency
            int_timestamp_utc = int(post['timestamp_utc'])
            new_post = Post(
                # post_title=post['post_title'],
                post_id=post['post_id'],
                subreddit=post['subreddit'],
                timestamp_utc=int_timestamp_utc,
                sentiment_label=post['mood'],
                sentiment_score=SENTIMENT_SCORES[post['label']],
                model_label=post['label'],
                model_confidence=post['score'],
            )
            db.session.add(new_post)
            db.session.commit()
            successfully_inserted_count += 1
        except Exception as e:
            not_inserted_count += 1
            db.session.rollback()
            print(
                f"Skipped duplicate or errored post_id {post['post_id']}: {e}")

    print(f'{successfully_inserted_count} posts inserted successfully.')
    return successfully_inserted_count, not_inserted_count
