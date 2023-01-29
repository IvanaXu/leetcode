class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        _max = 0
        for s in strs:
            try:
                r = int(s, 10)
            except:
                r = len(s)
            if r > _max:
                _max = r
        return _max
