#!/usr/bin/python3
"""
Script to convert a Markdown file to HTML, including heading parsing.
"""

import sys
import os

def parse_line(line):
    """
    Parse a single line of Markdown and convert it to HTML.
    Handles heading syntax from # to ######.
    """
    # Check for heading syntax (up to 6 levels)
    if line.startswith('#'):
        heading_level = len(line.split(' ')[0])  # Count the number of '#'
        if 1 <= heading_level <= 6:
            content = line[heading_level:].strip()  # Extract heading content
            return f"<h{heading_level}>{content}</h{heading_level}>"
    # Default: wrap content in a paragraph
    return f"<p>{line.strip()}</p>"

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert content
    try:
        with open(markdown_file, 'r') as md:
            lines = md.readlines()
    except Exception as e:
        print(f"Error reading {markdown_file}: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert each line to HTML
    html_content = "\n".join(parse_line(line) for line in lines)

    # Write the HTML content to the output file
    try:
        with open(html_file, 'w') as html:
            html.write(html_content)
    except Exception as e:
        print(f"Error writing to {html_file}: {e}", file=sys.stderr)
        sys.exit(1)

    # Exit successfully
    sys.exit(0)

