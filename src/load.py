import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import codecs
from database import DataBase
import config

def encode_utf8(string):
    return string.encode('utf-8')


def load_data_file():
    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " data.txt"
        raise Exception("failed")
    else:
        with codecs.open(sys.argv[1], encoding="utf-8") as file:
            text = []
            for line in file:
                text.append(encode_utf8(line))
            return text



if __name__ == "__main__":
    a = load_data_file()
    for l in a:
        pass
        # print l,
    db = DataBase(config.DDL_FILE, config.DB_FILE)
    sql = "insert into poetry(id, poet, dynasty, title, j1, j2, j3, j4) values(1, 'li bai', 'tang', 'kk', '1', '2', '3', '4');"
    db.execute(sql)
    sql = "select * from poetry;"
    a = db.execute(sql)
    print sql
    print a
