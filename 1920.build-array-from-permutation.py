class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[n]] for n in range(len(nums))]
