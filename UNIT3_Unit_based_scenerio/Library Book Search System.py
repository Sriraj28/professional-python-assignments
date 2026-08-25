import argparse
import csv
import sys

def load_books(filename):
    books = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(row)
        return books
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

def display_books(books):
    print("\n--- Library Catalog ---")
    for b in books:
        print(f"ISBN: {b.get('ISBN', 'N/A'):<10} | Title: {b.get('Title', 'N/A'):<20} | Author: {b.get('Author', 'N/A'):<15} | Status: {b.get('Status', 'Available')}")

def search_books(books, query):
    print(f"\n--- Search Results for '{query}' ---")
    matches = [
        b for b in books 
        if query.lower() in b.get('Title', '').lower() or query.lower() in b.get('Author', '').lower()
    ]
    if matches:
        for b in matches:
            print(f"Title: {b.get('Title')} | Author: {b.get('Author')} | Status: {b.get('Status', 'Available')}")
    else:
        print("No matching books found.")

def main():
    parser = argparse.ArgumentParser(description="Library Book Search System")
    parser.add_argument("--file", required=True, help="Path to books.csv file")
    parser.add_argument("--search", help="Search by Book Title or Author")
    args = parser.parse_args()

    books = load_books(args.file)

    if args.search:
        search_books(books, args.search)
    else:
        display_books(books)

if __name__ == "__main__":
    main()
