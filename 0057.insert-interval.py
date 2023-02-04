class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval) # NEW

        _r = []
        for n, v in enumerate(sorted(intervals)):
            if n == 0:
                _r.append(v)
            elif v[0] <= _r[-1][1]:
                _r[-1] = [_r[-1][0], max([v[1], _r[-1][1]])]
            else:
                _r.append(v)
        return _r
