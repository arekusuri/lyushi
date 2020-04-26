import sqlite3

class DataBase(object):
    def __init__(self, ddl, db=None):
        self.cnn = self._create_cnn(db)
        self._create_tables(ddl)

    def _create_cnn(self, file):
        if file is None:
            file = ':memory:'
        return sqlite3.connect(file)

    def _create_tables(self, ddl):
        with open(ddl) as file:
            text = file.readlines()
            sql = "".join(text)
            c = self.cnn.cursor()
            c.execute(sql)

    def execute(self, sql):
        c = self.cnn.cursor()
        t = c.execute(sql)
        return t.fetchone()

    def close(self):
        self.cnn.close()
