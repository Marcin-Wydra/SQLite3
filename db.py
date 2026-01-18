import sqlite3

class Database:
    def __init__(self, path):
        self.con = sqlite3.connect(path)

def connect_to_db(path):
    conn = sqlite3.connect(path)
    return conn

def create_table(self):
    query = "CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, \
             name TEXT NOT NULL, surname TEXT NOT NULL, date_joined DATETIME NOT NULL);"
    self.con.execute(query)

def add_to_customers(self, name, surname, date_joined):
    query = "INSERT INTO customers(name, surname, date_joined) VALUES (?, ?, ?)"
    self.con.execute(query, (name, surname, date_joined))

def preview_table(self, table_name):
    query = f'SELECT * FROM {table_name}'
    result = self.con.execute(query).fetchall()
    print(result)

def delete_from_customers(self, id):
    query = 'DELETE FROM customers WHERE id = ?'
    self.con.execute(query, (id, ))

def __enter__(self):
    return self

def __exit__(self, exc_type, exc_value, traceback):
    if isinstance(exc_type, Exception):
        self.con.rollback()
    else:
        self.con.commit()

    self.con.close()

with Database('example2-data.db') as db:
    db.create_table()
    db.add_to_customers('John', 'Wick', '2000-09-02')
    db.add_to_customers('James', 'Bond', '2002-05-16')
    db.preview_table('Customers')
    db.delete_from_customers(1)
    db.preview_table('Customers')

