# 📘 Manual Summary App

![WindowsPowerShell2025-11-2106-13-08-ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/d0cb4952-8b00-4879-92f3-680adf71f937)

This project takes an image-based user manual as input,
1. extracts text using OCR,
2. summarizes the key content into exactly three Korean sentences,
3. and converts the summary into a TTS (mp3) audio file.

The summarized text is used only during internal processing,
and the final output is the mp3 audio file.

---

## Project Structure

```
project_root/
│
│── app/
│     ├── __init__.py
│     ├── main.py                 # Runs the full pipeline
│     ├── ocr.py                  # Image → Text extraction
│     ├── summarizer.py           # Text summarization
│     ├── tts.py                  # Generate TTS audio
│
│── samples/
│     ├── sample_manual.jpg    
│     ├── sample_manual2.jpg      # Default image when no argument is given
│
│── .env                          # Stores API key (ignored by Git)
│── .gitignore                    # Excludes .env, output/, venv/, etc.
│── requirements.txt
│── README.md                             
```
---
## Environment

This project was developed and tested in the following environment:

- Python 3.10 (tested on 3.10.19)
- Operating System: Windows 10/11
- Required Libraries:
  - pytesseract
  - Pillow
  - openai
  - python-dotenv
  - gTTS

---
## Installation & Setup

### 1) Install required packages

```
pip install -r requirements.txt
```

### 2) Install Tesseract OCR (Windows)

* Download from: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
* Verify installation path:

```
C:\\Program Files\\Tesseract-OCR\\tesseract.exe
```

If the path is different, update `pytesseract.pytesseract.tesseract_cmd` in `ocr.py`.

---

## API Key Setup

The summarization feature uses the DeepSeek API.
Create a `.env` file in the project root and add:

```
DEEPSEEK_API_KEY=YOUR_KEY_HERE
```

This file is excluded by `.gitignore`, so it will **not** be uploaded to GitHub.

---

## How to Run

The main execution file is located in `app/main.py`.

### 1) Run using the default sample image

```
python -m app.main
```

→ Uses `samples/sample_manual2.jpg` automatically.


### 2) Run with a custom image

```
python -m app.main samples/your_image.jpg
```

Example:

```
python -m app.main samples/sample_manual.jpg
```

You must run the program from the project root folder.

---

## Pipeline Flow

1. **OCR — `extract_text()`**

   * Extracts text from the image using Tesseract.

2. **Summarization — `summarize_to_three_sentences()`**

   * Uses DeepSeek LLM to generate **exactly 3 Korean sentences**.

3. **TTS — `generate_tts()`**

   * Converts the summary into an MP3 file using gTTS.
   * Saved in the `output/` directory.

---

## Output Example

When executed, the console will display:

* Extracted raw text
* Final 3-sentence summary in Korean
* Generated MP3 file

---

## Notes

* `.env` must exist in the project root.
* Any relative or absolute image path can be used.
* OCR will fail if the Tesseract path is incorrect.

---

## Need Help?

If you want additional improvements or sections added to the README, feel free to ask!
leeyerin2697@kentech.ac.kr
