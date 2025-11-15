from paddleocr import PaddleOCR

# Initialize OCR model
ocr_model = PaddleOCR(lang='korean', use_angle_cls=True)

def extract_text(image_path: str) -> str:
    """
    Extract text from an image using PaddleOCR.
    Args:
        image_path (str): Path to the input image
    Returns:
        str: Extracted text
    """

    result = ocr_model.ocr(image_path)

    if not result:
        return ""

    lines = [line[1][0] for line in result[0]]
    return "\n".join(lines)
