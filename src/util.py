import re

def encode_utf8(string):
    return string.encode('utf-8')

def count_char(string):
    head1, head11, head111, head1111 = 0b10000000, 0b11000000, 0b11100000, 0b11110000
    count0, count1, count11, count111, count1111 = 0, 0, 0, 0, 0
    for c in string:
        num = ord(c)
        if head1 & num != 0:
            count1 += 1
        elif head11 & num != 0:
            count11 += 1
        elif head111 & num != 0:
            count111 += 1
        elif head1111 & num != 0:
            count1111 += 1
        else:
            count0 += 1
    return count0 + count11 + count111 + count1111


