import pytesseract
from pdf2image import convert_from_path
import cv2


def extract_text_from_image(image_path):
    try:
        image = cv2.imread(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error reading image : {e}"


def extract_text_from_pdf(pdf_path):
    try:
        pages = convert_from_path(pdf_path)
        text = " "
        for page in pages:
            text += pytesseract.image_to_string(page)
        return text
    except Exception as e:
        return f"Error reading PDF : {e}"
