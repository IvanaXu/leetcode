class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else:
            _c = sum([i < 0 for i in nums])%2 == 1
            return -1 if _c else 1
