import sqlite3
from sqlite3 import Error




class TodosSQL:
    # polączenie z bazą danych
    def __create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

# stworzenie nowej tabeli
    def __execute_sql(self, conn, sql):
        try:
            c = conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)

    def __init__(self):
        conn = self.__create_connection("todo.db")
        
    def all(self):
        conn = self.__create_connection("todo.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM todo")
        rows = cur.fetchall()
        return rows

    def get(self, id):
        conn = self.__create_connection("todo.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM todo WHERE id={id}")
        rows = cur.fetchall()
        id, title, description, done, token_crsf = rows[0]
        return {'title': title, 'description': description, 'done': int(done)}

    def create(self, data):
         
        conn = self.__create_connection("todo.db")
        sql = '''INSERT INTO todo(title, description, done, csrf_token)
                VALUES(?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    def update(self, id, data):
        conn = self.__create_connection("todo.db")
        
        values = tuple(v for v in data.values())
        values += (id, )
        sql = f''' UPDATE todo
                SET title = ?, description = ?, done = ?, csrf_token = ?
                WHERE id = ?'''
        try:
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            print("OK")
        except sqlite3.OperationalError as e:
            print(e)
        
todos = TodosSQL()