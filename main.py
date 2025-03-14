import sys
import time
from database import get_connection, create_table, create_index
from employee import Employee
from utils import generate_random_employees

LOG_FILE = "log.txt"

def log_result(mode, message, duration=None):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        if duration is not None:
            log.write(f"mode {mode}: {message} | Time: {duration:.4f} seconds\n")
        else:
            log.write(f"mode {mode}: {message}\n")

def main():
    conn = get_connection()

    if len(sys.argv) < 2:
        log_result("unknown", "No mode specified. Exiting.")
        print("Error: No mode specified. Please provide a mode (1-6).")
        return

    mode = sys.argv[1]
    start_time = time.time()

    try:
        if mode == '1':
            create_table(conn)
            duration = time.time() - start_time
            log_result(1, "Table created successfully.", duration)
            print("Table created successfully.")

        elif mode == '2':
            if len(sys.argv) < 5:
                log_result(2, "Not enough parameters for adding employee.")
                print("Error: Please provide full_name, birth_date, gender.")
                print('Example: python main.py 2 "Ivanov Petr Sergeevich" 2009-07-12 Male')
                return
            full_name, birth_date, gender = sys.argv[2], sys.argv[3], sys.argv[4]
            emp = Employee(full_name, birth_date, gender)
            emp.insert_into_db(conn)
            duration = time.time() - start_time
            log_result(2, f"Employee {full_name} added successfully.", duration)
            print("Employee added successfully.")

        elif mode == '3':
            cursor = conn.execute('SELECT DISTINCT full_name, birth_date, gender FROM employees ORDER BY full_name')
            for row in cursor:
                emp = Employee(*row)
                print(f"{emp.full_name}, {emp.birth_date}, {emp.gender}, Age: {emp.calculate_age()}")
            duration = time.time() - start_time
            log_result(3, "Employees list displayed.", duration)

        elif mode == '4':
            employees = generate_random_employees(1_000_000, include_special=True)
            Employee.bulk_insert(conn, employees)
            duration = time.time() - start_time
            log_result(4, "1,000,100 employees inserted successfully.", duration)
            print("Generated and inserted 1,000,100 employees.")

        elif mode == '5':
            cursor = conn.execute("SELECT full_name, birth_date, gender FROM employees WHERE gender='Male' AND full_name LIKE 'F%'")
            rows = cursor.fetchall()
            duration = time.time() - start_time
            for row in rows:
                print(row)
            log_result(5, f"Query executed. Records found: {len(rows)}", duration)
            print(f"Query time: {duration:.4f} seconds")

        elif mode == '6':
            create_index(conn)
            duration = time.time() - start_time
            log_result(6, "Index created successfully.", duration)
            print(f"Index created in {duration:.4f} seconds.")

        else:
            log_result(mode, "Invalid mode selected.")
            print("Invalid mode selected. Available modes: 1, 2, 3, 4, 5, 6.")

    except Exception as e:
        duration = time.time() - start_time
        log_result(mode, f"Error occurred: {str(e)}", duration)
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()