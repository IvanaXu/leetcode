class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for n, v in enumerate(nums):
            _nums = nums[:n] + nums[n+1:]
            
            if _nums == sorted(set(_nums)):
                return True
        return False
