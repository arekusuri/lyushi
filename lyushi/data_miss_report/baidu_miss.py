# -*- coding: utf-8 -*-
from config import config
from load_hanzi import get_hanzi_list
from load_data.pingshuiyun import Pingshuiyun

if __name__ == "__main__":
    config.set_pingshuiyun_data_file("/data/pingshuiyun-baidu.txt")
    hanzi_list = get_hanzi_list(config.TANGSHI_DATA_FILE, 11)
    pingshuiyun = Pingshuiyun(config.PINGSHUIYUN_DATA_FILE)
    ret = []
    for hanzi in hanzi_list:
        if hanzi not in pingshuiyun.pingze_info:
            ret.append(hanzi)
    print ret
