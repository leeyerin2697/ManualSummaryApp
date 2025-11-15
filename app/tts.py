from gtts import gTTS
import os
import time

def generate_tts(text, output_path="output"):
    """
    Generate TTS audio using gTTS and save as mp3.
    """
    os.makedirs(output_path, exist_ok=True)

    filename = f"{output_path}/summary_{int(time.time())}.mp3"

    tts = gTTS(text=text, lang='ko')
    tts.save(filename)

    return filename
