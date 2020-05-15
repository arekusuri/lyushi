import re

def encode_utf8(string):
    return string.encode('utf-8')

def count_char(string):
    cjkReg = re.compile(u'[\u1100-\uFFFDh]+?')
    trimedCJK = cjkReg.sub(' a ', string, 0)  # replace the CJK with the word a
    return len(trimedCJK.split())


