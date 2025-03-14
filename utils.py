import random
from datetime import datetime, timedelta
from employee import Employee

def random_date(start_year=1950, end_year=2005):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return (start + timedelta(days=random.randint(0, (end - start).days))).strftime("%Y-%m-%d")

def generate_random_employees(count, include_special=False):
    first_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    names = ['John', 'Alex', 'Chris', 'Mike', 'Sarah', 'Emma', 'Olivia', 'Sophia']
    employees = []

    for _ in range(count):
        letter = random.choice(first_letters)
        name = random.choice(names)
        surname = letter + "lastname"
        gender = random.choice(['Male', 'Female'])
        birth_date = random_date()
        employees.append(Employee(f"{surname} {name} Middle", birth_date, gender))

    if include_special:
        for _ in range(100):
            employees.append(Employee("Flastname John Middle", random_date(), "Male"))

    return employees