import os
from modules.pdf_converter import pdf_to_images
from modules.ocr_processor import extract_text_from_images
from modules.table_extractor import extract_tables_from_pdf
from modules.utils import save_to_csv

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # Step 1: Extract tables directly with Camelot
    print("Extracting tables from PDF...")
    table_files = extract_tables_from_pdf(pdf_path, output_folder)
    print(f"Extracted tables saved to: {table_files}")

    # Step 2: Convert PDF to images for OCR
    print("Converting PDF to images...")
    image_paths = pdf_to_images(pdf_path, output_folder)
    print(f"Images saved to: {image_paths}")

    # Step 3: Extract text from images using Tesseract
    print("Extracting text from images...")
    text_data = extract_text_from_images(image_paths, lang='eng')
    text_output_path = os.path.join(output_folder, "extracted_text.csv")

    # Step 4: Save extracted text to CSV
    print("Saving extracted text to CSV...")
    save_to_csv([[line] for line in text_data], text_output_path)
    print(f"Extracted text saved to: {text_output_path}")

if __name__ == "__main__":
    main()
