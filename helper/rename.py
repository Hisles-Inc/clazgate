import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        # Standardize the filename (remove extra spaces)
        cleaned_filename = filename.strip()

        # Match patterns like "chem-1-2015.pdf" or "OL-CHEM-2-2018.pdf"
        match = re.match(r'(?:(AL|al)[-_]?)?(?:chem(?:istry)?[-_]?)?(\d)[-_]?(\d{4})', cleaned_filename, re.IGNORECASE)
        
        # Match patterns like "OL-2022-CHEMISTRY-P1-Copy.pdf"
        match_alt = re.match(r'(?:AL[-_]?)?(\d{4})[-_]?CHEMISTRY[-_]?P?(\d)', cleaned_filename, re.IGNORECASE)

        if match:
            # Extract year and paper number from the first pattern
            exam_level = "OL"
            paper, year = match.groups()[1], match.groups()[2]
        elif match_alt:
            # Extract year and paper number from the second pattern
            year, paper = match_alt.groups()
            exam_level = "OL"
        else:
            # Skip files that do not match
            continue

        # Construct new filename
        new_name = f"{exam_level}-{year}-Chemistry-P{paper}.pdf"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

# Specify the directory containing the files
directory = "AL/Chemistry"  # Change this to the actual path
rename_files(directory)
