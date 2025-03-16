import os
import re
from collections import defaultdict

# Define the directory where files are stored
directory = "AL/Chemistry"
output_file = os.path.join(directory, "index.html")

# Read all files in the directory
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Dictionary to store files grouped by year
files_by_year = defaultdict(list)

# Regex pattern to extract the year from filenames
year_pattern = re.compile(r'(\d{4})')

# Group files by year
for file in files:
    match = year_pattern.search(file)
    if match:
        year = match.group(1)
        files_by_year[year].append(file)

# Sort years in descending order
sorted_years = sorted(files_by_year.keys(), reverse=True)

# Start building the HTML content
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download Chemistry Papers</title>
    
    <!-- Bootstrap CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Font Awesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; padding: 20px; background-color: #f8f9fa; }
        .container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        h1, h2 { text-align: center; color: #333; }
        .year-section { margin-bottom: 20px; }
        .file-list { list-style: none; padding: 0; }
        .file-item { display: flex; justify-content: space-between; align-items: center; padding: 10px; border-bottom: 1px solid #ddd; }
        .file-item:last-child { border-bottom: none; }
        .download-btn { text-decoration: none; color: white; }
    </style>
</head>
<body>

    <div class="container">
        <h1><i class="fas fa-file-download"></i> Chemistry Past Papers</h1>
"""

# Loop through sorted years and add file sections
for year in sorted_years:
    html_content += f"""
        <div class="year-section">
            <h2><i class="fas fa-calendar-alt"></i> {year}</h2>
            <ul class="file-list">
    """
    for file in files_by_year[year]:
        html_content += f"""
                <li class="file-item">
                    <span><i class="fas fa-file-pdf text-danger"></i> {file}</span>
                    <a href="{file}" download class="btn btn-primary btn-sm download-btn">
                        <i class="fas fa-download"></i> Download
                    </a>
                </li>"""
    html_content += """
            </ul>
        </div>
    """

# Close the HTML tags
html_content += """
    </div>

    <!-- Bootstrap JS (optional) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>"""

# Write the HTML content to the output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML file generated successfully: {output_file}")

