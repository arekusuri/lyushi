# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import codecs


class Pingshuiyun(object):
    _tone_info = dict([(u'上平', 0), (u'下平', 1), (u'上声', 2), (u'去声', 3), (u'入声', 4)])

    def __init__(self, pathfile):
        self.pathfile = pathfile
        self.ziyun_list = self._load_pingshuiyun()
        self.pingze_info, self.yunbu_info = self._build_pingze_yunbu_info()

    def _build_pingze_yunbu_info(self):
        pingze_info = {} # {u'字': [u'平', u'仄'] .... }
        yunbu_info = {} # {u'字': [u'十六谏', u'十八啸']}
        for ziyun in self.ziyun_list:
            # 平仄
            pingze_list = pingze_info.get(ziyun.hanzi, [])
            pingze = u'平' if ziyun.sheng <= 1 else u'仄'
            if pingze not in pingze_list:
                pingze_list.append(pingze)
            pingze_info[ziyun.hanzi] = pingze_list
            # 韵部
            yunbu_list = yunbu_info.get(ziyun.hanzi, [])
            yunbu = ziyun.yunbu
            yunbu_list.append(yunbu)
            yunbu_info[ziyun.hanzi] = yunbu_list
        return pingze_info, yunbu_info

    def _query_pingze_for_half(self, half_text):
        ret = []
        for hanzi in half_text:
            pingze_list = self.pingze_info.get(hanzi, [u'缺'])
            if len(pingze_list) > 1:
                ret.append(u'辨')
            else:
                ret.append(pingze_list[0])
        return ret

    def _query_yunbu(self, half_text):
        hanzi = half_text[-1]
        return self.yunbu_info.get(hanzi, [])

    def fulfill_pingze_yunbu(self, shi_list):
        for shi in shi_list:
            for half in shi.get_halfs():
                pingze = self._query_pingze_for_half(half._txt)
                yunbu = self._query_yunbu(half._txt)
                half.pingze = ''.join(pingze)
                half.yunbu = '; '.join(yunbu)
        return shi_list

    def _read_data_file(self):
        with codecs.open(self.pathfile, encoding="utf-8") as file:
            text = []
            for line in file:
                line = line.strip()
                text.append(line)
            return text

    def _parse_one(self, arr):
        text = "".join(arr)
        tone, yunbu, hanzi_str = text.split(',')
        yunbu = tone + ',' + yunbu
        sheng = self._tone_info[tone]
        ziyun_list = []
        hanzi_chrinfo = {}
        count = 0
        for i, hanzi in enumerate(hanzi_str):
            if hanzi == u'[' or (hanzi != u']' and count > 0):
                count += 1
            elif hanzi == u']':
                hanzi_chrinfo[hanzi] = count
                ziyun = ziyun_list[-1]
                ziyun.hanzi_descript = hanzi_str[i-count+1:i]
                count = 0
            else:
                ziyun = Ziyun(hanzi, sheng, yunbu)
                ziyun_list.append(ziyun)
        return ziyun_list

    def _load_pingshuiyun(self):
        ziyun_list = []
        text = self._read_data_file()
        start = 0
        for i in range(1, len(text)):
            line = text[i]
            first2chrs = line[:2]
            # if the current line starts with '上平', '下平'.. it is the end of current part
            if first2chrs in self._tone_info:
                arr = text[start : i] # slice the lines to make current part
                ziyun_list.extend(self._parse_one(arr))
                start = i
            # if the current line is last line, need to call parse_one as well
            if first2chrs in self._tone_info or i == len(text) - 1:
                arr = text[start: i+1]  # slice the lines to make current part
                ziyun_list.extend(self._parse_one(arr))
        return ziyun_list


class Ziyun(object):
    insert_sql = """insert into pingshuiyun(hanzi, sheng, yunbu, pingz) values(?, ?, ?, ?);"""
    def __init__(self, hanzi, sheng, yunbu, hanzi_descript = ""):
        self.hanzi = hanzi
        self.sheng = sheng
        self.yunbu = yunbu
        self.hanzi_descript = hanzi_descript

    def get_values(self):
        pingz = 0 if self.sheng <= 1 else 1
        return (self.hanzi, self.sheng, self.yunbu, pingz)
