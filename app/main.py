import sys
import os

# Force add project root to Python path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)

from app.ocr import extract_text
from app.summarizer import summarize_to_three_sentences
from app.tts import text_to_speech

def run_pipeline(image_path: str):
    print("=== Step 1: Extracting text with OCR ===")
    raw_text = extract_text(image_path)
    print(raw_text, "\n")

    print("=== Step 2: Summarizing to 3 sentences ===")
    summary = summarize_to_three_sentences(raw_text)
    print(summary, "\n")

    print("=== Step 3: Generating TTS audio ===")
    audio_path = text_to_speech(summary, "summary_output.mp3")
    print(f"Audio file saved as: {audio_path}")

if __name__ == "__main__":
    # sample image
    test_image = "samples/sample_manual.jpg"
    run_pipeline(test_image)
