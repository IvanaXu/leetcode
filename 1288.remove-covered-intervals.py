class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        _r, _intervals = [], sorted(intervals, key=lambda x: (x[0], -x[1]))
        for n, v in enumerate(_intervals):
            if n == 0:
                _r.append(v)
            elif _r[-1][0] <= v[0] <= v[1] <= _r[-1][1]:
                pass
            else:
                _r.append(v)
        return len(_r)
