Course = []
CourseID = []


class Courses:
    def __init__(self, cid, cname, ccredit):
        self._cid = cid
        self._cname = cname
        self._ccredit = ccredit
        Course.append(self)
        CourseID.append(self._cid)
        Credit.append(self._ccredit)

    def get_id(self):
        return self._cid

    def get_name(self):
        return self.cname

    def get_credit(self):
        return self._ccredit
