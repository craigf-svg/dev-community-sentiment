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

### Built Features
<details>
  <summary>Expand</summary>

  - Pulled top post data via PRAW from programming language subreddits

  - Sentiment analysis of top programming communities post titles

  - Leaderboard view ranking communities from most positive to most negative

  - MySQL database set up and populated with sample data

</details>

### Next-<i>ish</i> Steps
<details>
  <summary>Expand</summary>
  
  * **Write to Database**  
    Build a futureproof schema with consistent date handling

  * **Restructuring**  
    Separate analysis into its own microservice

  * **Automation**  
    Set up analysis microservice to run at least once a day

  * **Weekly analysis**  
    Design weekly leaderboard vs daily

  * **Include multiple leaderboards**  
    Expand to 3 leaderboards of 10 subreddits

</details>


### Ideas down the Pipeline
<details>
  <summary>Expand</summary>

  * **Caching via Redis**

  * **Deployment**

  * **Rolling 30-Day Memory of in-depth analysis**

  * **Dark Mode**

  * **Keyword Extraction**

</details>


## Setup

1. **Set up PRAW credentials in your .env (for live data)**

2. **Set Up environment from root folder**

    Make sure you have Python installed `python --version` | `python3 --version`

3. **Install dependencies**

    `pip install -r requirements.txt`

## Run the service

Start the Flask app `python server.py`

App runs on `http://127.0.0.1:5000`
