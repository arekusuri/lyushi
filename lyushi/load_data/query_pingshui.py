# -*- coding: utf-8 -*-

class QueryPingshui(object):
    def __init__(self, ziyun_list):
        self._pingze_info, self._yunbu_info = self._build_pingze_yunbu_info(ziyun_list)

    def _build_pingze_yunbu_info(self, ziyun_list):
        pingze_info = {} # {u'字': [u'平', u'仄'] .... }
        yunbu_info = {} # {u'字': [u'十六谏', u'十八啸']}
        for ziyun in ziyun_list:
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
            pingze_list = self._pingze_info.get(hanzi, [u'缺'])
            if len(pingze_list) > 1:
                ret.append(u'辨')
            else:
                ret.append(pingze_list[0])
        return ret

    def _query_yunbu(self, half_text):
        hanzi = half_text[-1]
        return self._yunbu_info.get(hanzi, [])

    def fulfill_pingze_yunbu(self, shi_list):
        for shi in shi_list:
            for half in shi.get_halfs():
                pingze = self._query_pingze_for_half(half._txt)
                yunbu = self._query_yunbu(half._txt)
                half.pingze = ''.join(pingze)
                half.yunbu = ', '.join(yunbu)
