from fetch_reddit.reddit_fetcher import fetch_story
from tts.hindi_tts import generate_hindi_voice
from utils.story_processor import summarize_story_for_shorts

if __name__ == "__main__":
    story = fetch_story()
    if story:
        print(f"\n📚 Subreddit: r/{story['subreddit']}")
        print(f"🧠 Title: {story['title']}\n")

        # Summarize the story
        summarized = summarize_story_for_shorts(story['title'], story['body'])
        print(f"\n📝 Summarized Story:\n{summarized}\n")
        
        if len(summarized.split()) < 10:
            print("❌ Summary too short! Skipping TTS.")
        else:
            generate_hindi_voice(summarized, speed=2.5)
