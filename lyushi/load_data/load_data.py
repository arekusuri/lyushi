from pingshuiyun import load_pingshuiyun
from tangshi import TangShiParser
from db_sqlite3 import DbSqlite3
import config


if __name__ == "__main__":
    db = DbSqlite3(config.DDL_FILE, config.DB_FILE)
    tangshi = TangShiParser()
    shi_arr = tangshi.parse()
    db.persistent_shi(shi_arr)
    ziyun_list = load_pingshuiyun()
    # todo calculate pingze
    db.persistent_pingshuiyun(ziyun_list)
    # print db.query("select * from half;")
    db.close()
