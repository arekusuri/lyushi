import sqlite3

sql = """
    insert into poetry(pid, author, dynasty, title, tiba, category)
    values(?, ?, ?);
"""

class DbSqlite3(object):
    def __init__(self, ddl, db=None):
        self.conn = self._create_cnn(db)
        self.cursor = self.conn.cursor()
        self._create_tables(ddl)

    def _create_cnn(self, file):
        if file is None:
            file = ':memory:'
        return sqlite3.connect(file)

    def _create_tables(self, ddl):
        with open(ddl) as file:
            text = file.readlines()
            sql_text = "".join(text)
            for sql in self._split_to_sqls(sql_text):
                self.cursor.execute(sql)

    def _split_to_sqls(self, sql_text):
        sqls = []
        for s in sql_text.split(";"):
            s = s.strip()
            if s:
                sqls.append(s + ";")
        return sqls

    def execute(self, sql):
        t = self.cursor.execute(sql)
        return t.fetchone()

    def store(self, shi_arr):
        for shi in shi_arr:
            values_to_insert = shi.get_values()
            self.cursor.execute(shi.insert_sql, values_to_insert)
            for half in shi.get_halfs():
                sql = half.insert_sql
                print sql
                print half.get_valus()
                self.cursor.execute(sql, half.get_valus())

    def close(self):
        self.cursor.close()
        self.conn.close()