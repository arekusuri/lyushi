import sys

from util import encode_utf8

reload(sys)
sys.setdefaultencoding('utf-8')

from tang_shi import TangShiParser


import codecs
from db_sqlite3 import DbSqlite3
import config



def load_data_file():
    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " data.txt"
        raise Exception("failed")
    else:
        with codecs.open(sys.argv[1], encoding="utf-8") as file:
            text = []
            for line in file:
                text.append(line)
            return text



if __name__ == "__main__":
    a = load_data_file()
    db = DbSqlite3(config.DDL_FILE, config.DB_FILE)
    tangshi = TangShiParser(a)
    shi_arr = tangshi.parse()
    db.store(shi_arr)
    db.close()
