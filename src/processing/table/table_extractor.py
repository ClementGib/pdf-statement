import re

from src.processing.ocr.ocr_processor import extract_text_from_image
from src.processing.text.text_adapter import extract_relevant_lines

def parse_table(body):
    """Parse the text to extract table rows."""
    rows = []
    current_row = {"date": None, "label": "", "value": None, "type": None}

    for line in body:
        # Regex to match rows starting with a date
        match = re.match(r"(\d{2}/\d{2}/\d{4})\s+(.+?)\s+([\d,]*)\s+([\d,]*)", line)

        if match:
            # If there's an existing row being constructed, finalize it
            if current_row["date"]:
                rows.append([
                    current_row["date"],
                    current_row["label"].strip(),
                    current_row["value"],
                    current_row["type"]
                ])

            # Extract the new row data
            date, label, debit, credit = match.groups()
            debit = debit.replace(',', '.').strip()
            credit = credit.replace(',', '.').strip()

            # Handle empty debit and credit fields
            value = (
                -float(debit) if debit else
                float(credit) if credit else
                0.0  # Default to 0.0 if both debit and credit are empty
            )

            txn_type = (
                "CHQ" if "CHQ" in label.upper() else
                "CARD" if "CARTE" in label.upper() else
                "RETRAIT" if "RETRAIT" in label.upper() else
                "VIR" if "VIR" in label.upper() else
                "OTHER"
            )

            current_row = {
                "date": date,
                "label": label.strip(),
                "value": value,
                "type": txn_type
            }
        else:
            # Add to the label of the current row if there's no new date
            current_row["label"] += " " + line.strip()

    # Append the last row after parsing all lines
    if current_row["date"]:
        rows.append([
            current_row["date"],
            current_row["label"].strip(),
            current_row["value"],
            current_row["type"]
        ])
    return rows

def extract_table(image):
    """Main method to extract the table from the image."""
    raw_text = extract_text_from_image(image)
    text_body = extract_relevant_lines(raw_text)
    table_data = parse_table(text_body)
    return table_data