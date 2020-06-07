# -*- coding: utf-8 -*-
import codecs

from etl.poetry_vo import Shi, Half


class TangShi(object):
    def __init__(self, filename):
        self.filename = filename
        self.text = self._load_data_file()
        self._data_start = self._find_start()
        self._data_end = len(self.text)
        self.shi_list = self._parse()

    def _parse(self):
        data_start, data_end = self._data_start, self._data_end
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
        return shi_arr

    def _find_start(self):
        """remove volume info for now"""
        count = 0
        while True:
            line = self.text[count].strip('\n')
            if line == "":
                count += 1
            elif line.startswith(u'卷') and '0' <= line[-1] <= '9':
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

    def _load_data_file(self):
        with codecs.open(self.filename, encoding="utf-8") as file:
            text = []
            for line in file:
                line = line.strip()
                text.append(line)
            return text

    def _parse_one(self, text):
        shi = Shi()
        for i in range(len(text)):
            line = text[i].strip()
            if not line:
                continue
            elif line[0].isdigit():
                pid, poet, title = self._parse_title(line)
                shi.set_pid_author_title("T" + str(pid), poet, title)
            elif len(line) > 16:
                shi._tiba += line
            else:
                end_symbol = line[-1]
                line = line[:-1]
                arr = line.split(u'，')
                if len(arr) == 2:
                    head_half = Half(arr[0], u"，")
                    tail_half = Half(arr[1], end_symbol)
                else:
                    arr = line.split(u'？')[0:2]
                    head_half = Half(arr[0], u"？")
                    tail_half = Half(arr[1], end_symbol)
                shi.add_half(head_half)
                shi.add_half(tail_half)
        return shi




