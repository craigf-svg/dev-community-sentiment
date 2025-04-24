# Sentiment Analysis of Programming Communities

A sentiment analysis service that tracks and ranks the sentiment of discussions across top programming language communities on Reddit.

🚧  This project is actively under development. 


| Technology              | Version   |
|------------------------------|---------------|
| Python                | 3.13.3       |
| MySQL                | 8.0.41       |
| HTMX                 | 1.9.10       |
| Transformers (HuggingFace) | 4.51.2     |
| PRAW (Python Reddit API Wrapper) | 7.8.1  |
| SQLAlchemy             | 2.0.40       |

## Built Features

- Pulled top post data via PRAW from programming language subreddits

- Sentiment analysis of top programming communities post titles

- Leaderboard view ranking communities from most positive to most negative

- MySQL database set up and populated with sample data


### What's Next

1. **Switch to comment analysis**
    
    Focus on analyzing comment content and aggregating sentiment.

2. **Tidy Up** 

    Clean up project structure and add tests for better maintainability and scalability.

3. **Dark Mode**

    Add dark mode theming and toggle.

4. **Real-Time Data Insertion**

   Currently analyzing in real time but not yet writing results into the database in real time.

5. **Scheduling / Automation** 

    Set up analysis to run every day automatically.

6. **Add Redis**

    Integrate Redis to improve performance performance and test speed differences 

### In the Pipeline
 
* **Deployment**

* **Rolling 30-Day Memory of in-depth analysis**

* **Keyword Extraction**


## Setup

1. **Set up PRAW credentials in your .env (for live data)**

2. **Set Up environment from root folder**

    Make sure you have Python installed `python --version` | `python3 --version`

3. **Install dependencies**

    `pip install -r requirements.txt`

## Run the service

Start the Flask app `python server.py`

App runs on `http://127.0.0.1:5000`