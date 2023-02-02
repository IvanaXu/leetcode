# Python2
_r = set()
        for e in emails:
            [e0, e1] = e.split("@")
            _r.add("{0}@{1}".format(e0.replace('.','').split('+')[0], e1))
        return len(_r)

# Python3
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        _r = set()
        for e in emails:
            [e0, e1] = e.split("@")
            _r.add(f"{e0.replace('.','').split('+')[0]}@{e1}")
        return len(_r)
