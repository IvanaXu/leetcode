class Solution:
    def reformat(self, s: str) -> str:
        _rc, _rn = [], []
        for i in s:
            if i in "0123456789":
                _rn.append(i)
            else:
                _rc.append(i)
        #
        _r, _lc, _ln = [], len(_rc), len(_rn)
        if (_lc == 0 and _ln > 1) or (_ln == 0 and _lc > 1):
            return ""
        elif abs(_lc-_ln) > 1:
            return ""
        elif _lc > _ln:
            _r = [_rc[0]]
            for i in range(_ln):
                _r.extend([_rn[i], _rc[i+1]])
        elif _lc == _ln:
            for i in range(_lc):
                _r.extend([_rc[i], _rn[i]])
        elif _lc < _ln:
            _r = [_rn[0]]
            for i in range(_lc):
                _r.extend([_rc[i], _rn[i+1]])
        return "".join(_r)
