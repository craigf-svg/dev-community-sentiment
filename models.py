from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    post_id = db.Column(db.String(12), nullable=False, unique=True)
    subreddit = db.Column(db.String(255), nullable=False)
    timestamp_utc = db.Column(db.BigInteger, nullable=False)
    # Positive, Negative, or Neutral
    sentiment_label = db.Column(db.String(20))
    sentiment_score = db.Column(db.SmallInteger)  # +1, -1, 0
    model_label = db.Column(db.String(20))  # LABEL_0, LABEL_2, LABEL_1
    # Range of [0-1.0] confidence in label
    model_confidence = db.Column(db.Float)
    # Generated columns
    post_date_utc = db.Column(db.Date, db.FetchedValue())
    post_date_est = db.Column(db.Date, db.FetchedValue())

    def __repr__(self):
        return f"<Post {self.post_id} - {self.subreddit}>"

    def to_dict(self):
        return {
            'post_id': self.post_id,
            'subreddit': self.subreddit,
            # Convert Unix timestamp
            'timestamp_utc': self.timestamp_utc,
            'post_date_utc': self.post_date_utc.strftime('%Y-%m-%d') if self.post_date_utc else None,
            'post_date_est': self.post_date_est.strftime('%Y-%m-%d') if self.post_date_est else None,
            'sentiment_label': self.sentiment_label,
            'sentiment_score': self.sentiment_score,
            'model_label': self.model_label,
            'model_confidence': self.model_confidence
        }


class FetchLog(db.Model):
    __tablename__ = 'fetch_log'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    created_at_utc = db.Column(
        db.TIMESTAMP, nullable=False, server_default=db.func.now())
    created_date_est = db.Column(db.Date, db.FetchedValue())
    created_date_utc = db.Column(db.Date, db.FetchedValue())
    inserted_post_count = db.Column(db.Integer, default=0)
    skipped_duplicate_post_count = db.Column(db.Integer, default=0)
    duration_seconds = db.Column(db.Float)
    status = db.Column(db.String(20), nullable=False, default='success')

    def __repr__(self):
        return (
            f"<FetchLog id={self.id} status={self.status} "
            f"inserted_post_count={self.inserted_post_count}>"
        )

    def to_dict(self):
        return {
            'id': self.id,
            'created_at_utc': self.created_at_utc.isoformat() if self.created_at_utc else None,
            'created_date_est': self.created_date_est.strftime('%Y-%m-%d') if self.created_date_est else None,
            'created_date_utc': self.created_date_utc.strftime('%Y-%m-%d') if self.created_date_utc else None,
            'inserted_post_count': self.inserted_post_count,
            'skipped_duplicate_post_count': self.skipped_duplicate_post_count,
            'duration_seconds': self.duration_seconds,
            'status': self.status
        }
