from config import config
from etl.db_sqlite3 import DbSqlite3
from etl.load_pingze_proof import load_proof
from etl.pingshuiyun import Pingshuiyun
from etl.tangshi import TangShi

if __name__ == "__main__":
    db = DbSqlite3(config.DDL_FILE, config.DB_FILE)

    pingshuiyun = Pingshuiyun(config.PINGSHUIYUN_DATA_FILE)
    db.persistent_pingshuiyun(pingshuiyun.ziyun_list)

    tangshi = TangShi(config.TANGSHI_DATA_FILE)
    pingshuiyun.fulfill_pingze_yunbu(tangshi.shi_list)
    db.persistent_shi(tangshi.shi_list)

    pingze_list = load_proof()
    db.persistent_proof(pingze_list)

    db.close()
