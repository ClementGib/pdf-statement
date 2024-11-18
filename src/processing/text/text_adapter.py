def extract_relevant_lines(raw_text):
    """
    Extract all lines between 'operation' and 'Aréception'.
    :param raw_text: A single string containing all text.
    :return: List of relevant lines.
    """
    if not raw_text:
        raise ValueError("The raw_text string is empty or None.")

    # Split the string into lines
    lines = raw_text.splitlines()

    start_index = None
    end_index = None

    # Find the starting index after "opération"
    for i, line in enumerate(lines):
        if "opération" in line:
            start_index = i + 1
            break

    # Find the ending index at the first occurrence of "A réception"
    for i, line in enumerate(lines):
        if "À réception" in line:
            end_index = i
            break

    if start_index is None:
        raise ValueError("'operation' not found in the raw_text string.")
    if end_index is None:
        raise ValueError("'A réception' not found in the raw_text string.")

    # Extract and return the relevant lines
    return lines[start_index:end_index]
