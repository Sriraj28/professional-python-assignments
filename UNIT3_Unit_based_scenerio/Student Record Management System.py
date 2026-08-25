import argparse
import csv
import sys

def read_records(filename):
    records = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                records.append(row)
        return records
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

def display_all(records):
    print("\n--- All Student Records ---")
    for r in records:
        print(f"Roll No: {r.get('RollNo', r.get('roll_no', 'N/A')):<6} | Name: {r.get('Name', r.get('name', 'N/A')):<15} | Marks: {r.get('Marks', r.get('marks', 'N/A'))}")

def search_by_roll(records, roll_no):
    print(f"\n--- Search Result for Roll No: {roll_no} ---")
    for r in records:
        if r.get('RollNo') == roll_no or r.get('roll_no') == roll_no:
            print(f"Record Found -> Name: {r.get('Name', r.get('name'))} | Marks: {r.get('Marks', r.get('marks'))}")
            return
    print("Student record not found.")

def main():
    parser = argparse.ArgumentParser(description="Student Record Management System")
    parser.add_argument("--file", required=True, help="Path to students.csv file")
    parser.add_argument("--search", help="Search by Roll Number")
    args = parser.parse_args()

    records = read_records(args.file)
    
    if args.search:
        search_by_roll(records, args.search)
    else:
        display_all(records)

if __name__ == "__main__":
    main()
