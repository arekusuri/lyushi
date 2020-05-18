from query_pingshui import QueryPingshui
from pingshuiyun import load_pingshuiyun
from tangshi import TangShiParser
from db_sqlite3 import DbSqlite3
import config


if __name__ == "__main__":
    db = DbSqlite3(config.DDL_FILE, config.DB_FILE)

    ziyun_list = load_pingshuiyun()
    db.persistent_pingshuiyun(ziyun_list)

    tangshi = TangShiParser()
    shi_list = tangshi.parse()
    pingshui_helper = QueryPingshui(ziyun_list)
    pingshui_helper.fulfill_pingze_yunbu(shi_list)
    db.persistent_shi(shi_list)
    db.close()
