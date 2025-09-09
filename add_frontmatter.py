#!/usr/bin/env python3

import os
import re
from pathlib import Path


def add_frontmatter_to_feedback(file_path):
    """Add Jekyll front matter to a feedback.md file if it doesn't already have it."""

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if front matter already exists
    if content.startswith("---"):
        print(f"Front matter already exists in {file_path}")
        return

    # Extract student name from directory path
    student_name = file_path.parent.name

    # Extract the title from the first heading
    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    if title_match:
        title = title_match.group(1)
    else:
        title = f"{student_name} Web Design Project Feedback"

    # Create front matter
    front_matter = f"""---
layout: feedback
title: "{title}"
description: "Detailed feedback for {student_name}'s Flask web development project"
---

"""

    # Add front matter to the beginning of the file
    new_content = front_matter + content

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Added front matter to {file_path}")


def main():
    """Process all feedback.md files in student directories."""

    base_dir = Path(".")

    # Find all feedback.md files in student directories (directories starting with capital letters)
    for feedback_path in base_dir.glob("[A-Z]*/feedback.md"):
        add_frontmatter_to_feedback(feedback_path)


if __name__ == "__main__":
    main()
