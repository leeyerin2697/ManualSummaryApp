from app.ocr import extract_text
from app.summarizer import summarize_to_three_sentences
from app.tts import generate_tts

def run_pipeline(image_path):
    print("=== Step 1: Extracting text with OCR ===")   #extract text
    raw_text = extract_text(image_path)
    print(raw_text)

    print("\n=== Step 2: Summarizing to 3 sentences ===")   #summarize
    summary = summarize_to_three_sentences(raw_text)
    print(summary)

    print("\n=== Step 3: Generating Audio ===")             #change it to sound
    output_path = generate_tts(summary)
    print(f"TTS saved to: {output_path}")

if __name__ == "__main__":
    test_image = "samples/sample_manual.jpg"   # test image path
    run_pipeline(test_image)
