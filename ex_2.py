import sqlite3

class Notebook:
    def __init__(self, path):
        self.con = sqlite3.connect(path)

    def connect_to_db(path):
        con = sqlite3.connect(path)
        return con

    def create_table(self):
        query = ("CREATE TABLE IF NOT EXISTS Note(id INTEGER PRIMARY KEY, \
                 title TEXT UNIQUE NOT NULL, note_content TEXT NOT NULL, \
                 created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")
        self.con.execute(query)

    def add_note(self, title, note_content):
        query = ("INSERT INTO Note(title, note_content) "
                 "VALUES (?, ?)")
        self.con.execute(query, (title, note_content))

    def delete_note(self, title):
        query = "DELETE FROM Note WHERE title = ?"
        self.con.execute(query, (title,))

    def print_notes(self):
        query = "SELECT * FROM NOTE "
        print(self.con.execute(query).fetchall())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if isinstance(exc_type, Exception):
            self.con.rollback()
        else:
            self.con.commit()

        self.con.close()

with Notebook('notebook.db') as db:
    db.create_table()
    db.add_note('Note1', 'Notatka numer 1')
    db.add_note('Note2', 'Notatka numer 2')
    db.print_notes()
    db.delete_note('Note1')
    db.print_notes()

