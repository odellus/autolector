import time
import sqlite3

# Set up sqllite3 db class.
class AutolectorDB:
    '''
    A neat little DB class so we know it disconnects because __del__
    '''
    db_file = 'autolector.db'
    table_name = 'autolector'
    dt_pattern = '%Y-%m-%d %H:%M:%S'

    def __init__(self):
        '''
        Get a connection to self.db_file and create a cursor
        '''
        self.connection = sqlite3.connect(self.db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def save(self):
        '''
        Have to do this after everything apparently.
        '''
        self.connection.commit()

    def insert(self, question, context, answer):
        '''
        Insert question, context, answer, and timestamp into the table.
        '''
        date = time.strftime(self.dt_pattern)
        qry = "INSERT INTO autolector VALUES (?, ?, ?, ?)"
        self.cursor.execute(qry, (date, question, context, answer))
        self.save()

    def get_all(self):
        '''
        Return all the rows in the self.table_name table.
        '''
        qry = f'SELECT * FROM {self.table_name}'
        rows = [x for x in self.cursor.execute(qry)]
        return rows

    def create_table(self):
        '''
        Creates a table named self.table_name: default-> autolector.
        '''
        qry = f'''CREATE TABLE {self.table_name}
                 (date text, question text, context text, answer text)'''
        self.cursor.execute(qry)

    def drop_table(self):
        '''
        Drop table self.table_name from database.
        '''
        qry = f"DROP TABLE {self.table_name}"
        self.cursor.execute(qry)

    def __del__(self):
        '''
        The whole reason we are using OOP. Close connection automatically.
        '''
        self.save()
        self.connection.close()
