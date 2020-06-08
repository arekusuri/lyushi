from config import config
from etl.db_sqlite3 import DbSqlite3


def load_proof():
    with open(config.PROOF_FILE) as file:
        pingze_list = []
        for line in file:
            line = line.strip()
            if line.startswith("-"):
                continue
            arr = line.split("|")
            if len(arr) == 5:
                pingze_list.append((arr[0], arr[2], arr[4]))
        return pingze_list

if __name__ == "__main__":
    db = DbSqlite3(config.DDL_FILE, config.DB_FILE)
    pingze_list = load_proof()
    db.persistent_proof(pingze_list)
    db.close()
