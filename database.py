import sqlite3

def get_connection(db_name="employees.db"):
    return sqlite3.connect(db_name)

def create_table(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                gender TEXT NOT NULL
            )
        ''')

def create_index(conn):
    with conn:
        conn.execute('CREATE INDEX IF NOT EXISTS idx_gender_name ON employees (gender, full_name)')