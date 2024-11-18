import pytesseract
from PIL import Image

def extract_text_from_images(image_paths, lang='eng'):
    text_data = []
    for image_path in image_paths:
        text = pytesseract.image_to_string(Image.open(image_path), lang=lang)
        text_data.append(text)
    return text_data
