# Sentiment Analysis of Programming Communities

A sentiment analysis service that tracks and ranks the sentiment of discussions across top programming language communities on Reddit.

🚧  This project is actively under development. 


<p align="center">
  <strong>
    System Architecture Diagram
  </strong>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/91414292-44f8-4da6-ae5a-20b181567c68" alt="Architecture Diagram" />
</p>

## Built Features

* Fetch top posts from programming language subreddits using PRAW
* Perform sentiment analysis on post titles
* Display a leaderboard ranking communities from most positive to most negative
* Write analysis results and post information to MySQL database
* Log relevant information for each run, including timestamps and inserted/skipped post counts


<i><strong>In progress</strong></i>

* Write analysis duration and status to fetch log entries

### Next-<i>ish</i> Steps
<details>
  <summary>Expand</summary>
  
* Separate the PRAW processor into its own service
* Infrastructure for the analysis microservice to run daily
* Multiple Leaderboards
* Weekly view for leaderboards
</details>


### Ideas down the Pipeline
<details>
  <summary>Expand</summary>
  
  * Caching via Redis
  * Deployment
  * Rolling 30-Day in-depth analysis memory
  * Keyword Extraction
</details>

| Technology              | Version   |
|------------------------------|---------------|
| Python                | 3.13.3       |
| MySQL                | 8.0.41       |
| HTMX                 | 1.9.10       |
| Transformers (HuggingFace) | 4.51.2     |
| PRAW (Python Reddit API Wrapper) | 7.8.1  |
| SQLAlchemy             | 2.0.40       |

## Setup

1. **Add PRAW credentials in your .env (for live data)**

2. **Make sure you have Python installed `python --version` | `python3 --version`**

3. **Install dependencies**

    `pip install -r requirements.txt`

## Run the service

Start the Flask app `python server.py`

App runs on `http://127.0.0.1:5000`
