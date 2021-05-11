Mark = []
ccredit = []
gpa = []


class Marks:
    def __init__(self, mid, nid, mark, gpa):
        self._mid = mid
        self._nid = nid
        self._mark = mark
        self._gpa = gpa
        mark.append(self)

    def get_mid(self):
        return self.mid

    def get_nid(self):
        return self.nid

    def get_mark(self):
        return self.mark

    def get_gpa(self):
        return self.gpa
