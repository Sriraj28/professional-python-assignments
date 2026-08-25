import argparse
import csv
import sys

def load_employees(filename):
    employees = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
        return employees
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

def display_employees(employees):
    print("\n--- Employee Records ---")
    for emp in employees:
        print(f"ID: {emp.get('EmpID', emp.get('emp_id', 'N/A')):<6} | Name: {emp.get('Name', emp.get('name', 'N/A')):<15} | Department: {emp.get('Department', emp.get('dept', 'N/A')):<12} | Salary: ₹{emp.get('Salary', emp.get('salary', 'N/A'))}")

def search_employee(employees, emp_id):
    print(f"\n--- Search Result for Employee ID: {emp_id} ---")
    for emp in employees:
        if emp.get('EmpID') == emp_id or emp.get('emp_id') == emp_id:
            print(f"Employee Found -> Name: {emp.get('Name', emp.get('name'))} | Dept: {emp.get('Department', emp.get('dept'))} | Salary: ₹{emp.get('Salary', emp.get('salary'))}")
            return
    print("Employee ID not found.")

def main():
    parser = argparse.ArgumentParser(description="Employee Record Management System")
    parser.add_argument("--file", required=True, help="Path to employee.csv file")
    parser.add_argument("--search", help="Search by Employee ID")
    args = parser.parse_args()

    employees = load_employees(args.file)

    if args.search:
        search_employee(employees, args.search)
    else:
        display_employees(employees)

if __name__ == "__main__":
    main()
