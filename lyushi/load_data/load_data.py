from pingshuiyun import Pingshuiyun
from tangshi import TangShi
from db_sqlite3 import DbSqlite3
import config


if __name__ == "__main__":
    db = DbSqlite3(config.DDL_FILE, config.DB_FILE)

    pingshuiyun = Pingshuiyun(config.PINGSHUIYUN_DATA_FILE)
    db.persistent_pingshuiyun(pingshuiyun.ziyun_list)

    tangshi = TangShi(config.TANGSHI_DATA_FILE)
    pingshuiyun.fulfill_pingze_yunbu(tangshi.shi_list)
    db.persistent_shi(tangshi.shi_list)
    db.close()