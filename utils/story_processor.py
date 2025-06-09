from openai import OpenAI
import os

# Load API key from environment variable (recommended)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_story_for_shorts(title, body, language="hindi", target_duration=30):
    prompt = f"""
You are a YouTube Shorts scriptwriter. Summarize the following Reddit story to fit a {target_duration}-second Hindi storytelling video. Use natural, conversational Hindi, and keep it engaging. Avoid NSFW content.

Title: {title}

Body: {body}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a Hindi storyteller."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=250
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"❌ Error summarizing: {e}")
        return title  # fallback if summary fails
