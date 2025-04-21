from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ORM for a basic subreddit_sentiment table
class SubredditSentiment(db.Model):
    __tablename__ = 'subreddit_sentiment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subreddit = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    avg_sentiment = db.Column(db.Numeric(5, 2)) 
    total_comments = db.Column(db.Integer)
    top_keywords = db.Column(db.Text)

    def __repr__(self):
        return f"<SubredditSentiment {self.subreddit} - {self.date}>"
