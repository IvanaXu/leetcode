# Python2
class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        _r = ""
        _st, _sn = "", 0
        for s in S+"/":
            if s != _st:
                _r += "{0}{1}".format(_st,_sn) if _sn > 0 else ""
                _st, _sn = s, 1
            else:
                _sn += 1
        return _r if len(_r) < len(S) else S

# Python3
class Solution:
    def compressString(self, S: str) -> str:
        _r = ""
        _st, _sn = "", 0
        for s in S+"/":
            if s != _st:
                _r += f"{_st}{_sn}" if _sn > 0 else ""
                _st, _sn = s, 1
            else:
                _sn += 1
        return _r if len(_r) < len(S) else S
