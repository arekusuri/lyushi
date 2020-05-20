import codecs

def _load_data_file(pathfile):
    with codecs.open(pathfile, encoding="utf-8") as file:
        text = []
        for line in file:
            line = line.strip()
            text.append(line)
        return text

def get_hanzi_list(pathfile, start_line):
    arr = _load_data_file(pathfile)
    text = "".join(arr)
    for k in text:
        print k
    hanzi_set = set(list(text))
    hanzi_list = []
    for hanzi in hanzi_set:
        hanzi_list.append(hanzi)
    hanzi_list.sort()
    return hanzi_list