import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

# stworzenie nowej tabeli
def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

sql= """
        CREATE TABLE IF NOT EXISTS todo (
        id integer PRIMARY KEY,
        title text NOT NULL,
        description VARCHAR(250) NOT NULL,
        done text,
        csrf_token text
    );
    """

db_file = 'todo.db'

conn = create_connection(db_file)
if conn is not None:
    execute_sql(conn, sql)