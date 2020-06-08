import os

WORK_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../"

class Config(object):
    def __init__(self):
        self.PINGSHUIYUN_DATA_FILE = WORK_DIR + "data/pingshuiyun-baidu.txt"
        self.TANGSHI_DATA_FILE = WORK_DIR + "data/tangshi300.txt"
        self.DB_FILE = WORK_DIR + "var/lyushi.db"
        self.DDL_FILE = WORK_DIR + "ddl/ddl.sql"
        self.PROOF_FILE = WORK_DIR + "data/stage-2/proofread.txt"

    def set_pingshuiyun_data_file(self, pathfile):
        config.PINGSHUIYUN_DATA_FILE = WORK_DIR + pathfile

config = Config()

