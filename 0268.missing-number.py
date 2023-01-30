class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # 2172 ms
        # _n = len(nums)
        # for i in range(0, _n+1):
        #     if i not in nums:
        #         return i
        # return _n+1

        # # 40ms
        _nums = [i for i in range(0, len(nums)+1)]
        for n in nums:
            _nums[n] = 1
        return reduce(lambda x, y: x*y, _nums)
