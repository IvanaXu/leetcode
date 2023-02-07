class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        _r = set()
        for n in nums:
            if n not in _r:
                _r.add(n)
            else:
                return n
