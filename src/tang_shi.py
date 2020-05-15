# -*- coding: utf-8 -*-
import sys

from shi import Shi
from util import encode_utf8, count_char

reload(sys)
sys.setdefaultencoding('utf-8')


class TangShiParser(object):
    def __init__(self, text):
        self.text = text
        self.data_start = self._find_start()
        self.data_end = len(text)
        pass

    def _find_start(self):
        """remove volume info for now"""
        count = 0
        while True:
            line = self.text[count].strip('\n')
            if line == "":
                count += 1
            elif line.startswith(encode_utf8('卷')) and '0' <= line[-1] <= '9':
                count += 1
            elif line[0] == ' ' and '0' <= line[-1] <= '9':
                count += 1
            else:
                break
        return count

    def _parse_title(self, line):
        n = int(line[:3])
        arr = line.split("：")
        return (n, arr[0][3:], arr[1])

    def parse(self):
        data_start, data_end = self.data_start, self.data_end
        start = data_start
        shi_arr = []
        for i in range(data_start, data_end):
            line = self.text[i].strip()
            if line != "" and line[0].isdigit():
                if i != data_start:
                    one_shi = self.text[start: i]
                    shi = self._parse_one(one_shi)
                    shi_arr.append(shi)
                    start = i

    def _parse_one(self, text):
        shi = Shi()
        sentences = []
        for i in range(len(text)):
            line = self.text[i].strip()
            if not line:
                continue
            elif line[0].isdigit():
                n, poet, title = self._parse_title(line)
                shi.set_num_author_title(n, poet, title)
            elif count_char(line) > 16:
                shi.note += line
            else:
                arr = line.split(encode_utf8('，'))
                sentences.extend(arr)
        shi.set_sentences(len(sentences), sentences)
        return shi
