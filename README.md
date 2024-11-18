# PDF statements to Table Converter

This tool allow me to extract incoming/outgoing transaction table of a bank statements

## Features
- Extracts structured tables using Camelot.
- Converts PDFs to images for OCR-based text extraction.
- Saves extracted data into CSV format.

## Requirements
- Python 3.x
- Tesseract OCR (Install via system package manager)

## Setup
1. Clone this repository.
2. Install dependencies:


Tesseract:
```bash
sudo apt install tesseract-ocr  # Linux
brew install tesseract          # macOS
```

Create a Virtual Environment:

```bash
python3 -m venv venv
```

Activate the Virtual Environment:
```bash
source venv/bin/activate
```
You should now see (venv) in your terminal prompt.


Install Packages in the Virtual Environment:

```bash
pip install -r requirements.txt
```


```bash
python src/main.py
```

Exit:

```bash
deactivate
```