
class Shi(object):
    def __init__(self):
        self.number = 0
        self.title = ""
        self.note = ""
        self.author = ""
        self.dynasty = ""
        self.categroy = 0
        self.total = 0
        self.halfs = []
        self.symbols = []

    def set_num_author_title(self, num, author, title):
        self.number, self.author, self.title = num, author, title

    def set_sentences(self, arr):
        self.halfs = arr
        self.total = len(arr)
