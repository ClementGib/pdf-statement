from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder):
    """
    Converts a PDF to images, one per page.

    Args:
        pdf_path (str): Path to the PDF.
        output_folder (str): Folder to save the images.
        poppler_path (str): Path to Poppler binaries.

    Returns:
        list: List of image paths.
    """
    poppler_path='/opt/homebrew/bin'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to images
    images = convert_from_path(pdf_path, poppler_path=poppler_path)

    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.jpg")
        image.save(image_path, "JPEG")
        image_paths.append(image_path)

    return image_paths
