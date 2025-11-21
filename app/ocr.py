import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (required on Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Perform OCR on the image using multiple languages
    # (Korean, English, Simplified Chinese, Traditional Chinese, Japanese)
    text = pytesseract.image_to_string(img, lang='eng')

    # Return the extracted text
    return text
