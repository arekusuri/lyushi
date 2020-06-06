# -*- coding: utf-8 -*-
from config import config
from data_miss_report.load_hanzi import get_hanzi_list
from etl.pingshuiyun import Pingshuiyun

if __name__ == "__main__":
    config.set_pingshuiyun_data_file("/data/pingshuiyun-baidu.txt")
    hanzi_list = get_hanzi_list(config.TANGSHI_DATA_FILE)
    pingshuiyun = Pingshuiyun(config.PINGSHUIYUN_DATA_FILE)
    ret = []
    for hanzi in hanzi_list:
        if hanzi not in pingshuiyun.pingze_info:
            ret.append(hanzi)
