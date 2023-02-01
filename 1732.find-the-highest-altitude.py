class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        _r = [0]
        for g in gain:
            _r.append(_r[-1] + g)
        return max(_r)
