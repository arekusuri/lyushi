import sys

from util import encode_utf8

reload(sys)
sys.setdefaultencoding('utf-8')

from tang_shi import TangShiParser


import codecs
from database import DataBase
import config



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
    # db = DataBase(config.DDL_FILE, config.DB_FILE)
    tangshi = TangShiParser(a)
    tangshi.parse()
    for l in tangshi.text:
        print l
        pass
    sql = "insert into poetry(id, poet, dynasty, title, j1, j2, j3, j4) values(1, 'li bai', 'tang', 'kk', '1', '2', '3', '4');"
    # db.execute(sql)
    sql = "select * from poetry;"
    # a = db.execute(sql)
    print sql
    print a
