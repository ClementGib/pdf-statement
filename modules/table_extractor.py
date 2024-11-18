import camelot

def extract_tables_from_pdf(pdf_path, output_folder):
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')  # Use 'lattice' for bordered tables
    extracted_files = []
    for i, table in enumerate(tables):
        output_file = f"{output_folder}/table_{i + 1}.csv"
        table.to_csv(output_file)
        extracted_files.append(output_file)
    return extracted_files
