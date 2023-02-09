class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        INF = float("-inf")
        nums = [INF] + nums + [INF]
        _l = len(nums)
        for i in range(_l-3+1):
            [v0, v1, v2] = nums[i:i+3]
            if v1 > v0 and v1 > v2:
                return i
