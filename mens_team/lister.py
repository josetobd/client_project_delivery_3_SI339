import os

# Define the directory where your HTML files are located
directory = 'mens_team'  # Adjust this to your directory if needed
out_directory= 'xc_data-main'

# Initialize the html_content variable with the starting HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/style.css">
    <title>Men Page</title>
</head>
<body>
    <h1>Men's Homepage</h1>
    <ul>
"""

# Scan through the directory and find .html files
for file_name in os.listdir(directory):
    if file_name.endswith(".html"):
        # Encode spaces in file names for URLs
        file_name_escaped = file_name.replace(" ", "%20")
        # Generate relative path
        relative_path = f'/{directory}/{file_name_escaped}'
        # Add each file as a link with the relative path
        html_content += f'<li><a href="{relative_path}" target="_blank">{file_name}</a></li>\n'

# Close the HTML structure
html_content += """
    </ul>
    </nav>
    <footer>
        <p>&copy; 2024 Your Website. All rights reserved.</p>
        <p><a href="#">Contact Us</a></p>
    </footer>
</body>
</html>
"""

# Write the generated HTML to a file
output_file = os.path.join(directory, 'list_of_html_files.html')
with open(output_file, 'w') as file:
    file.write(html_content)

print(f"HTML file listing all .html files has been created: {output_file}")
