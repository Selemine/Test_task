from datetime import datetime

class Employee:
    def __init__(self, full_name, birth_date, gender):
        self.full_name = full_name
        self.birth_date = birth_date
        self.gender = gender

    def insert_into_db(self, conn):
        with conn:
            conn.execute('INSERT INTO employees (full_name, birth_date, gender) VALUES (?, ?, ?)', 
                         (self.full_name, self.birth_date, self.gender))

    def calculate_age(self):
        birth = datetime.strptime(self.birth_date, "%Y-%m-%d")
        today = datetime.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    @staticmethod
    def bulk_insert(conn, employees_list):
        with conn:
            conn.executemany('INSERT INTO employees (full_name, birth_date, gender) VALUES (?, ?, ?)', 
                             [(e.full_name, e.birth_date, e.gender) for e in employees_list])