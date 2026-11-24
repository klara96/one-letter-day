#!/usr/bin/env python3
"""
Write the make.fun competition entry text to a file.

The entry is '<<<R>>>' (one letter standing for the word 'ratelimited').
The output directory is controlled by MAKEFUN_OUTPUT_DIR (default: /output).
"""
import os
import sys

ENTRY_TEXT = "<<<R>>>\n"

def main():
    # Get output directory from environment or default to /output
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "entry.txt")
    
    # Write entry text exactly as specified
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    
    print(f"Written to {output_path}")

if __name__ == "__main__":
    main()
