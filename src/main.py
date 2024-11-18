from src.processing.file.image_processor import preprocess_image
from src.processing.file.pdf_converter import pdf_to_images
from src.processing.table.table_extractor import extract_table
from src.utils.utils import save_to_csv, clean_folder


def main():
    # Paths
    pdf_path = "../statements/bourso-bank/02-23-checking-perso.pdf"
    output_folder = "../output/"
    output_csv = "../output/extracted_data.csv"

    clean_folder(output_folder) # debug with images
    # Step 1: Convert PDF to images
    print("Converting PDF to images...")
    image_paths = pdf_to_images(pdf_path, output_folder)
    print(f"Images saved to: {image_paths}")

    # Step 2: Extract text from images
    print("Extracting statements from images...")
    all_table_data = []
    for image_path in image_paths:
        # text = extract_text_from_image(image_path, lang='fra')
        image = preprocess_image(image_path)
        table = extract_table(image)
        all_table_data.extend(table)

    # clean_folder(output_folder) # clean folder
    # Step 3: Save extracted data to CSV
    print("Saving extracted data to CSV...")
    save_to_csv(all_table_data, output_csv)

if __name__ == "__main__":
    main()
