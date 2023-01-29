class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return sorted(nums, key=lambda x: (abs(x), -x))[0]
