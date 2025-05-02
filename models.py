from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Float, Date
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    post_id = db.Column(db.String(12), nullable=False, unique=True)
    subreddit = db.Column(db.String(255), nullable=False)
    timestamp_utc = db.Column(db.DateTime, nullable=False)
    post_date_utc = db.Column(db.Date, nullable=False,
                              default=db.func.current_date())
    post_date_est = db.Column(db.Date, nullable=False)
    sentiment_label = db.Column(db.String(20)) # Positive, Negative, or Neutral
    sentiment_score = db.Column(db.SmallInteger) # +1, -1, 0
    model_label = db.Column(db.String(20)) # LABEL_0, LABEL_2, LABEL_1
    model_confidence = db.Column(db.Float) # Range of [0-1.0] confidence in label

    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.text("CURRENT_TIMESTAMP"))
    created_at_est = db.Column(db.Date, default=db.text(
        "CONVERT_TZ(created_at, 'UTC', 'America/New_York')"))

    def __repr__(self):
        return f"<Post {self.post_id} - {self.subreddit}>"

    def to_dict(self):
        return {
            'post_id': self.post_id,
            'subreddit': self.subreddit,
            'timestamp_utc': self.timestamp_utc.strftime('%Y-%m-%d %H:%M:%S') if self.timestamp_utc else None,
            'post_date_utc': self.post_date_utc.strftime('%Y-%m-%d') if self.post_date_utc else None,
            'post_date_est': self.post_date_est.strftime('%Y-%m-%d') if self.post_date_est else None,
            'sentiment_label': self.sentiment_label,
            'sentiment_score': self.sentiment_score,
            'model_label': self.model_label,
            'model_confidence': self.model_confidence
        }
