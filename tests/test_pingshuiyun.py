# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase

from load_data import config
from load_data.pingshuiyun import Pingshuiyun
from load_data.poetry_vo import Shi, Half


class TestPingshuiyun(TestCase):
    def test_fulfill_pingze_yunbu(self):
        pingshuiyun = Pingshuiyun(config.PINGSHUIYUN_DATA_FILE)
        shi = Shi()
        half = Half(u'夫子何为者', '')
        shi.add_half(half)
        pingshuiyun.fulfill_pingze_yunbu([shi])
        half = shi.get_halfs()[0]
        pz = half.pingze
        self.assertEqual(pz, u'平仄平平辨')

    def test__build_pingze_yunbu_info(self):
        pingshuiyun = Pingshuiyun(config.PINGSHUIYUN_DATA_FILE)
        pingze_info, _ = pingshuiyun._build_pingze_yunbu_info()
        pz1 = pingze_info[u'何']
        self.assertEqual(pz1, [u'平'])
        pz2 = pingze_info[u'间']
        self.assertEqual(pz2, [u'平'])


if __name__ == '__main__':
    unittest.main()

