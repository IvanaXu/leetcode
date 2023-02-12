class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # [[1,2],[2,3],[3,5]]
        # [[1,2],[2,3],[2,5]]
        # [[1,2],[3,4],[5,6]]
        _n, _lv = 0, -9999
        for _v in sorted(pairs, key=lambda x: x[1]):
            if _lv == -9999 or _v[0] > _lv:
                _n += 1
                _lv = _v[1]
        return _n
