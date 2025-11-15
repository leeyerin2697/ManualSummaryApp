import sys
from app.ocr import extract_text
from app.summarizer import summarize_to_three_sentences
from app.tts import generate_tts

def run_pipeline(image_path):
    print("=== Step 1: Extracting text with OCR ===")
    raw_text = extract_text(image_path)
    print(raw_text)
    print()

    print("=== Step 2: Summarizing to 3 sentences ===")
    summary = summarize_to_three_sentences(raw_text)
    print(summary)
    print()

    print("=== Step 3: Generating Audio ===")
    output_path = generate_tts(summary)
    print(f"TTS saved to: {output_path}")


if __name__ == "__main__":
    # Default image or user-provided
    if len(sys.argv) >= 2:
        image_path = sys.argv[1]
    else:
        image_path = "samples/sample_manual2.jpg"

    run_pipeline(image_path)
