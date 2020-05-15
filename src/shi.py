
class Shi(object):
    def __init__(self):
        self.number = 0
        self.title = ""
        self.note = ""
        self.author = ""
        self.dynasty = ""
        self.categroy = 0
        self.total = 0
        self.j1 = ""
        self.j2 = ""
        self.j3 = ""
        self.j4 = ""
        self.j5 = ""
        self.j6 = ""
        self.j7 = ""
        self.j8 = ""

    def set_num_author_title(self, num, author, title):
        self.number, self.author, self.title = num, author, title

    def set_sentences(self, total, arr):
        self.j1, self.j2, self.j3, self.j4 = arr[:4]
        if total == 8:
            self.j5, self.j6, self.j7, self.j8 = arr[4:]
