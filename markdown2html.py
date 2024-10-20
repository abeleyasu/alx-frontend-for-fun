#!/usr/bin/python3
"""
Script to convert a Markdown file to HTML, including headings and unordered lists.
"""

import sys
import os

def parse_lines(lines):
    """
    Parse the lines of Markdown and convert them to HTML.
    Handles headings and unordered lists.
    """
    html_lines = []
    in_list = False  # Track if we are inside an <ul> block

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace

        # Check for heading syntax (up to 6 levels)
        if line.startswith('#'):
            heading_level = len(line.split(' ')[0])  # Count the number of '#'
            content = line[heading_level:].strip()  # Extract heading content
            html_lines.append(f"<h{heading_level}>{content}</h{heading_level}>")

        # Check for unordered list item
        elif line.startswith('- '):
            if not in_list:
                html_lines.append("<ul>")  # Start a new <ul> block
                in_list = True
            content = line[2:].strip()  # Extract list item content
            html_lines.append(f"<li>{content}</li>")

        else:
            # Close the <ul> block if we are currently inside one
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            # Wrap non-heading, non-list lines in <p> tags
            if line:
                html_lines.append(f"<p>{line}</p>")

    # Close any remaining <ul> block
    if in_list:
        html_lines.append("</ul>")

    return "\n".join(html_lines)

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
            lines = md.readlines()
    except Exception as e:
        print(f"Error reading {markdown_file}: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert lines to HTML
    html_content = parse_lines(lines)

    # Write the HTML content to the output file
    try:
        with open(html_file, 'w') as html:
            html.write(html_content)
    except Exception as e:
        print(f"Error writing to {html_file}: {e}", file=sys.stderr)
        sys.exit(1)

    # Exit successfully
    sys.exit(0)

