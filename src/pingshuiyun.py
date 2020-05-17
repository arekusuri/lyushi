# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
import config


class Ziyun(object):
    insert_sql = """insert into pingshuiyun(hanzi, sheng, yunbu, pingz) values(?, ?, ?, ?);"""
    def __init__(self, hanzi, sheng, yunbu):
        self.hanzi = hanzi
        self.sheng = sheng
        self.yunbu = yunbu

    def get_values(self):
        pingz = 0 if self.sheng <= 1 else 1
        return (self.hanzi, self.sheng, self.yunbu, pingz)


def _read_data_file():
    with codecs.open(config.PINGSHUIYUN_DATA_FILE, encoding="utf-8") as file:
        text = []
        for line in file:
            line = line.strip()
            text.append(line)
        return text

_tone_info = dict([
    (u'上平', 0),
    (u'下平', 1),
    (u'上声', 2),
    (u'去声', 3),
    (u'入声', 4),
])


def _parse_one(arr):
    text = "".join(arr)
    tone, yunbu, hanzi_str = text.split(',')
    sheng = _tone_info[tone]
    ziyun_list = []
    for hanzi in hanzi_str:
        ziyun = Ziyun(hanzi, sheng, yunbu)
        ziyun_list.append(ziyun)
    return ziyun_list


def load_pingshuiyun():
    ziyun_list = []
    text = _read_data_file()
    start = 0
    for i in range(1, len(text)):
        line = text[i]
        if line[:2] in _tone_info:
            arr = text[start : i]
            ziyun_list.extend(_parse_one(arr))
            start = i
    return ziyun_list

