import praw
import random
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

subreddit_pool = [
    'ShortScaryStories',
    'Glitch_in_the_Matrix',
    'TIFU',
    'TodayILearned',
    'HumansBeingBros'
]

def get_rotating_subreddit():
    return random.choice(subreddit_pool)

def fetch_story(limit=25, min_length=300):
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

    subreddit_name = get_rotating_subreddit()
    subreddit = reddit.subreddit(subreddit_name)
    
    print(f"🔍 Searching in r/{subreddit_name}...")

    # Get top posts of all time
    for post in subreddit.top(time_filter='all', limit=limit):
        if post.selftext and not post.over_18 and len(post.selftext.strip()) >= min_length:
            return {
                'title': post.title,
                'body': post.selftext.strip(),
                'subreddit': subreddit_name,
                'url': post.url
            }

    return None
