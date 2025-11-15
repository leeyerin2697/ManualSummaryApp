from gtts import gTTS

def text_to_speech(text: str, output_path: str = "summary.mp3") -> str:
    """
    Convert Korean summary text into a spoken audio file using gTTS.
    
    Args:
        text (str): The summary text to convert into speech.
        output_path (str): Path where the audio file will be saved.
        
    Returns:
        str: The path to the generated audio file.
    """

    tts = gTTS(text=text, lang="ko")
    tts.save(output_path)

    return output_path
