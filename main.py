from fetch_reddit.reddit_fetcher import fetch_story

if __name__ == "__main__":
    story = fetch_story()
    if story:
        print(f"🎯 Subreddit: r/{story['subreddit']}")
        print(f"🧠 Title: {story['title']}")
        print(f"📜 Body:\n{story['body'][:1000]}...")
    else:
        print("❌ No suitable story found.")
