# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase

from config import config
from etl.pingshuiyun import Pingshuiyun
from etl.poetry_vo import Shi, Half


class TestPingshuiyun(TestCase):
    def test_fulfill_pingze_yunbu(self):
        pingshuiyun = Pingshuiyun(config.PINGSHUIYUN_DATA_FILE)
        shi = Shi()
        half = Half(u'夫子何为者', '')
        shi.add_half(half)
        pingshuiyun.fulfill_pingze_yunbu([shi])
        half = shi.get_halfs()[0]
        pz = half.pingze
        self.assertEqual(pz, u'平仄平辨仄')

    def test__build_pingze_yunbu_info(self):
        pingshuiyun = Pingshuiyun(config.PINGSHUIYUN_DATA_FILE)
        pingze_info, _ = pingshuiyun._build_pingze_yunbu_info()
        pz1 = pingze_info[u'何']
        self.assertEqual(pz1, [u'平'])
        pz2 = pingze_info[u'间']
        self.assertEqual(pz2, [u'平', u'仄'])

    def test_fulfill_pingze_yunbu(self):
        pingshuiyun = Pingshuiyun(config.PINGSHUIYUN_DATA_FILE)
        shi = Shi()
        half = Half(u'干', '')
        shi.add_half(half)
        pingshuiyun.fulfill_pingze_yunbu([shi])
        half = shi.get_halfs()[0]
        pz = half.pingze
        self.assertEqual(pz, u'辨')

    def test__parse_one(self):
        pingshuiyun = Pingshuiyun(config.PINGSHUIYUN_DATA_FILE)
        ziyun_list = pingshuiyun._parse_one(u'上平,十四寒,寒韩翰[翰韵同]丹单安鞍难[艰难]餐檀坛滩弹残干肝竿阑栏澜兰看[翰韵同]刊丸完桓纨端湍酸团攒官观[观看]鸾銮峦冠[衣冠]欢宽盘蟠漫[大水貌]叹[翰韵同]邯郸摊玕拦珊狻鼾杆跚姗殚箪瘅谰獾倌棺剜潘拼[问韵同]盘般蹒瘢磐瞒谩馒鳗钻抟邗汗[可汗]')
        ziyun_list = pingshuiyun._parse_one(u'上平,十四寒,干')


if __name__ == '__main__':
    unittest.main()


