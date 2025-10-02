from PyPDF2 import PdfReader
import pytesseract
from pdf2image import convert_from_bytes

def extract_text_from_pdf(uploaded_file):
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        if text.strip():
            return text
        # Si no hay texto, aplicar OCR
        uploaded_file.seek(0)
        images = convert_from_bytes(uploaded_file.read())
        text_ocr = ""
        for img in images:
            text_ocr += pytesseract.image_to_string(img)
        return text_ocr
    except Exception:
        return ""
