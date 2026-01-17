import sqlite3

def connect_to_db(path):
    conn = sqlite3.connect(path)
    return conn

def create_table(conn):
    query = "CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, \
             name TEXT NOT NULL, surname TEXT NOT NULL, date_joined DATETIME NOT NULL);"
    conn.execute(query)
    conn.commit()

def add_to_customers(conn, name, surname, date_joined):
    query = "INSERT INTO customers(name, surname, date_joined) VALUES (?, ?, ?)"
    conn.execute(query, (name, surname, date_joined))
    conn.commit()

conn = connect_to_db("example-database.sqlite3")
create_table(conn)
add_to_customers(conn, 'John', 'Wick', '2000-09-02')
add_to_customers(conn, 'James', 'Bond', '2002-05-16')

def preview_table(conn, table_name):
    query = f'SELECT * FROM {table_name}'
    result = conn.execute(query).fetchall()
    print(result)

preview_table(conn, 'Customers')