# Reddit YouTube Shorts Generator

This project automates the process of fetching interesting stories from Reddit, summarizing them for YouTube Shorts in Hindi, generating Hindi voiceovers, and preparing them for video creation and upload.

## Features
- **Fetches stories** from popular subreddits using Reddit API (via PRAW)
- **Summarizes stories** for YouTube Shorts using OpenAI GPT models
- **Translates and generates Hindi voiceovers** using Google Text-to-Speech (gTTS) and Deep Translator
- **Prepares content** for video creation and upload

## Project Structure
```
main.py                  # Entry point for the workflow
config.py                # Stores API keys and configuration
requirements.txt         # Main dependencies
requirements_full.txt    # All installed packages (for full reproducibility)
.env                     # Environment variables (API keys, secrets)
fetch_reddit/
    reddit_fetcher.py    # Fetches stories from Reddit
utils/
    story_processor.py   # Summarizes stories using OpenAI
    translator.py        # (Optional) Translation utilities
video_generator/
    video_creator.py     # (Optional) Video creation logic
uploader/
    youtube_uploader.py  # (Optional) Uploads videos to YouTube
output/                  # Stores generated audio files
```

## Setup
1. **Clone the repository**
2. **Install dependencies**
   - For main dependencies:
     ```sh
     pip install -r requirements.txt
     ```
   - For full reproducibility:
     ```sh
     pip install -r requirements_full.txt
     ```
3. **Configure environment variables**
   - Copy `.env` and fill in your API keys:
     - `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USER_AGENT`
     - `OPENAI_API_KEY`
     - `YOUTUBE_CLIENT_SECRET_FILE` (if uploading to YouTube)

## Usage
Run the main script:
```sh
python main.py
```
This will:
- Fetch a story from a random subreddit
- Summarize it for a Hindi YouTube Short
- Generate a Hindi voiceover and save it to the `output/` folder

## Requirements
- Python 3.10+
- See `requirements.txt` or `requirements_full.txt`

## Notes
- Ensure you have valid API keys in your `.env` file.
- The project avoids NSFW content and aims for engaging, conversational Hindi.
- You can extend the workflow to generate videos and upload to YouTube.

## Credits
- [PRAW](https://praw.readthedocs.io/) for Reddit API
- [OpenAI](https://platform.openai.com/docs/api-reference) for summarization
- [gTTS](https://gtts.readthedocs.io/) and [Deep Translator](https://pypi.org/project/deep-translator/) for Hindi TTS

---
Feel free to contribute or adapt for your own use!
