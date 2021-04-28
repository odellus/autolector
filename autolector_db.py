import time
import sqlite3

# Set up sqllite3 db class.
class AutolectorDB:
    db_file = 'autolector.db'
    dt_pattern = '%Y-%m-%d %H:%M:%S'
    def __init__(self):
        self.connection = sqlite3.connect(self.db_file, check_same_thread=False)
        self.get_cursor()
    def get_cursor(self):
        self.cursor = self.connection.cursor()
    def save(self):
        self.connection.commit()
    def insert(self, question, context, answer):
        date = time.strftime(self.dt_pattern)
        qry = "INSERT INTO autolector VALUES (?, ?, ?, ?)"
        self.cursor.execute(qry, (date, question, context, answer))
        self.save()
    def get_all(self):
        qry = 'SELECT * FROM autolector'
        rows = [x for x in self.cursor.execute(qry)]
        return rows
    def create_table(self):
        qry = '''CREATE TABLE autolector
                 (date text, question text, context text, answer text)'''
        self.cursor.execute(qry)
    def drop_table(self, table_name):
        qry = f"DROP TABLE {table_name}"
        self.cursor.execute(qry)
    def __del__(self):
        self.save()
        self.connection.close()
