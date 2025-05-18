#!/usr/bin/env python3
"""
Regex Data Extractor
Extracts various data types from a text file using regular expressions.
"""

import re
import time


def read_file(filename="form.txt"):
    """Reads and returns the contents of the specified file."""
    with open(filename, "r") as file:
        return file.read()


def extract_emails(text):
    """Extracts email addresses from text."""
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return re.findall(pattern, text)


def extract_urls(text):
    """Extracts URLs from text."""
    pattern = r"https?://[^\s]+"
    return re.findall(pattern, text)


def extract_phone_numbers(text):
    """Extracts phone numbers in various formats."""
    pattern = r"(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}"
    return re.findall(pattern, text)


def extract_credit_cards(text):
    """Extracts credit card numbers with spaces or dashes."""
    pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    return re.findall(pattern, text)


def extract_times(text):
    """Extracts times in 12-hour or 24-hour format."""
    pattern = r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?: ?[AaPp][Mm])?\b"
    return re.findall(pattern, text)


def extract_html_tags(text):
    """Extracts HTML tags."""
    pattern = r"</?[a-zA-Z][a-zA-Z0-9]*\b[^>]*>"
    return re.findall(pattern, text)


def extract_hashtags(text):
    """Extracts hashtags."""
    pattern = r"#\w+"
    return re.findall(pattern, text)


def extract_currency_amounts(text):
    """Extracts currency amounts (dollars) like $1,234.56."""
    pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
    return re.findall(pattern, text)


def print_results(items, item_type):
    """Prints extracted items or a message if none found."""
    if items:
        print(f"\nFound {len(items)} {item_type}:")
        for item in items:
            print(f" - {item}")
    else:
        print(f"No {item_type} found.")


def main():
    content = read_file()

    menu = {
        "1": ("Emails", extract_emails),
        "2": ("URLs", extract_urls),
        "3": ("Phone numbers", extract_phone_numbers),
        "4": ("Credit cards", extract_credit_cards),
        "5": ("Times", extract_times),
        "6": ("Currency amounts", extract_currency_amounts),
        "7": ("Hashtags", extract_hashtags),
        "8": ("HTML tags", extract_html_tags),
        "9": ("Exit", None),
    }

    while True:
        print("\n--- Regex Data Extractor ---\n")
        for key, (name, _) in sorted(menu.items()):
            print(f"{key}. Find {name}")

        choice = input("\nEnter your choice (1-9): ").strip()

        if choice not in menu:
            print("Invalid choice. Please enter a number between 1 and 9.")
            continue

        if choice == "9":
            print("Exiting... Goodbye!")
            break

        item_name, func = menu[choice]
        print(f"\nExtracting {item_name}...\n")
        time.sleep(1)

        results = func(content)
        print_results(results, item_name.lower())


if __name__ == "__main__":
    main()
