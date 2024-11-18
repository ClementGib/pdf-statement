import cv2
import os

import numpy as np


def preprocess_image(image_path):
    """Load and preprocess the image."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at path: {image_path}")

    print(f"Loading image from: {image_path}")
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not load image from path: {image_path}")

    print("Converting image to grayscale...")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou Gaussien pour réduire le bruit (optionnel)
    # blurred = cv2.GaussianBlur(gray, (5, 5), 0)


    # Augmenter le contraste à l'aide de l'égalisation d'histogramme NOT GOOD
    # equalized = cv2.equalizeHist(gray)

    # Appliquer le seuillage adaptatif
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 15, 4)

    # Appliquer une fermeture morphologique avec un noyau plus petit
    kernel = np.ones((2, 2), np.uint8)
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    _, image = cv2.threshold(closed, 150, 255, cv2.THRESH_BINARY)

    preprocess_path = image_path
    cv2.imwrite(preprocess_path, closed)
    return closed