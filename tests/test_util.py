#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from unittest import TestCase
import unittest
from load_data.util import count_char

class Test(TestCase):
    def test_count_char(self):
        n = count_char(u"海上生明月")
        self.assertEqual(n, 5)

    def test_count_char12(self):
        n = count_char(u'夫子何为者，栖栖一代中。')
        self.assertEqual(n, 12)



    def test_count_char_ascii(self):
        n = count_char(u"aaa")
        self.assertEqual(n, 3)


if __name__ == '__main__':
    unittest.main()
