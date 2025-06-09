from gtts import gTTS
import os
import uuid
from pydub import AudioSegment
from deep_translator import GoogleTranslator

def translate_to_hindi(text):
    try:
        translated = GoogleTranslator(source='auto', target='hi').translate(text)
        if not translated or len(translated.strip()) < 10:
            raise Exception("Translation failed or empty.")
        return translated
    except Exception as e:
        print(f"❌ Translation error: {e}")
        return text  # fall back to original (should still be good)


def change_speed(audio_path, speed=1.5):
    sound = AudioSegment.from_file(audio_path)
    new_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    }).set_frame_rate(sound.frame_rate)

    new_path = audio_path.replace(".mp3", f"_fast.mp3")
    new_sound.export(new_path, format="mp3")
    return new_path

def generate_hindi_voice(text, output_dir="output", lang="hi", speed=2.0):
    os.makedirs(output_dir, exist_ok=True)
    print(f"📢 Original text to speak:\n{text}\n")

    # Translation + check
    hindi_text = translate_to_hindi(text)
    print(f"🌐 Translated to Hindi:\n{hindi_text}\n")

    
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{uuid.uuid4().hex[:8]}.mp3"
    filepath = os.path.join(output_dir, filename)

    hindi_text = translate_to_hindi(text)

    try:
        tts = gTTS(text=hindi_text, lang=lang, slow=False)
        tts.save(filepath)
        print(f"✅ Saved voice to {filepath}")
        if speed > 1.0:
            filepath = change_speed(filepath, speed)
            print(f"🚀 Voice speed increased: {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ Error generating voice: {e}")
        return None
