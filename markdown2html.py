#!/usr/bin/python3
"""
Script to convert a Markdown file to HTML.
"""

import sys
import os

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

    # Read the Markdown file
    try:
        with open(markdown_file, 'r') as md:
            content = md.read()
    except Exception as e:
        print(f"Error reading {markdown_file}: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to simple HTML (for now, just a paragraph)
    html_content = f"<p>{content.strip()}</p>"

    # Write the HTML content to the output file
    try:
        with open(html_file, 'w') as html:
            html.write(html_content)
    except Exception as e:
        print(f"Error writing to {html_file}: {e}", file=sys.stderr)
        sys.exit(1)

    # Exit successfully
    sys.exit(0)
