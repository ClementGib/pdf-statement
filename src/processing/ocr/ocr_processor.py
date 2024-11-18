def extract_text_from_image(image, lang='fra'):
    import pytesseract
    # Extract text
    custom_config = "--oem 3 --psm 6"  # Set Tesseract to assume a table-like structure
    text = pytesseract.image_to_string(image, lang=lang, config=custom_config)
    return text
