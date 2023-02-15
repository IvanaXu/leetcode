class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        _sl, _sr = 0, sum(nums)
        for n, v in enumerate(nums):
            _sr -= v
            if _sl == _sr:
                return n
            _sl += v
        return -1
