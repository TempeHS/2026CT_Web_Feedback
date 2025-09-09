#!/usr/bin/env python3

import os
import re
from pathlib import Path


def escape_jinja_syntax(content):
    """Escape Jinja2 template syntax in markdown content for Jekyll processing."""

    # Escape all {% ... %} tags by wrapping them in backticks for inline code
    content = re.sub(r"\{\%[^%]*\%\}", lambda m: f"`{m.group(0)}`", content)

    # Escape all {{ ... }} variable syntax by wrapping in backticks
    content = re.sub(r"\{\{[^}]*\}\}", lambda m: f"`{m.group(0)}`", content)

    return content


def process_feedback_file(file_path):
    """Process a feedback.md file to escape Jinja2 syntax."""

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip files that don't contain Jinja2 syntax
    if not re.search(r"\{\%|\{\{", content):
        print(f"No Jinja2 syntax found in {file_path}")
        return

    # Process the content
    original_content = content
    processed_content = escape_jinja_syntax(content)

    # Only write if content changed
    if processed_content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(processed_content)
        print(f"Escaped Jinja2 syntax in {file_path}")
    else:
        print(f"No changes needed in {file_path}")


def main():
    """Process all feedback.md files in student directories."""

    base_dir = Path(".")

    # Find all feedback.md files in student directories (directories starting with capital letters)
    for feedback_path in base_dir.glob("[A-Z]*/feedback.md"):
        process_feedback_file(feedback_path)


if __name__ == "__main__":
    main()
