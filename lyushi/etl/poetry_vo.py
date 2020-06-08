class Shi(object):
    insert_sql = """
        insert into poetry(pid, dynasty, author, title, tiba)
        values(?, ?, ?, ?, ?);
    """
    def __init__(self):
        self._pid = ""
        self._dynasty = ""
        self._author = ""
        self._title = ""
        self._tiba = ""
        self._halfs = []

    def add_half(self, half):
        half._pid = self._pid
        half.order_num = len(self._halfs) + 1
        self._halfs.append(half)

    def set_pid_author_title(self, pid, author, title):
        self._pid = pid
        self._author = author
        self._title = title

    def get_values(self):
        return (
            self._pid,
            self._dynasty,
            self._author,
            self._title,
            self._tiba
        )

    def get_halfs(self):
        return self._halfs

class Half(object):
    insert_sql = """
        insert into half(pid, txt, flg, order_num, zishu, pingze_auto, pingze, yunbu)
        values(?, ?, ?, ?, ?, ?, ?, ?);
    """
    def __init__(self, txt, flg):
        self._txt = txt
        self._flg = flg
        self.order_num = 0
        self.zishu = len(txt)
        self._pid = ""
        self.pingze_auto = ""
        self.pingze = ""
        self.yunbu = ""

    def get_valus(self):
        return (self._pid, self._txt, self._flg, self.order_num, self.zishu, self.pingze_auto, self.pingze, self.yunbu)

