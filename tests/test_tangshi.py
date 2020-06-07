import unittest
from unittest import TestCase, mock

from etl.tangshi import TangShi


class TestTangShi(TestCase):
    pass

    @mock.patch('etl.tangshi.TangShi', autospec=True)
    def test__parse_one(self, mock_shi):
        text = [u"160李商隐：北青萝",
                u"",
                u"落叶人何在？寒云路几层？",
                ]
        shi = mock_shi.return_value
        shi._parse_title.return_value = ("1", "poet", "title")
        shi._parse_one = TangShi._parse_one
        a = TangShi._parse_one(shi, text)
        self.assertEqual(a.get_halfs()[1]._txt, u"寒云路几层")
        self.assertEqual(a.get_halfs()[1]._flg, u"？")


if __name__ == '__main__':
    unittest.main()
