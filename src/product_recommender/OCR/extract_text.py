import pytesseract
from pytesseract import Output
from PIL import Image

def extract_text(img_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text  = pytesseract.image_to_string(img_path,lang='eng')
    return text