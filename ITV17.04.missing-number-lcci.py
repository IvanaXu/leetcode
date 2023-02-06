class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 数列
        _l = len(nums)
        _sum = (1 + _l) * _l//2
        for i in nums:
            _sum -= i
        return _sum
