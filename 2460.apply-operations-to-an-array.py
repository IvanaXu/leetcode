class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        _l = len(nums)
        for n in range(_l-1):
            if nums[n] == nums[n+1]:
                nums[n] = 2 * nums[n]
                nums[n+1] = 0
        return sorted(nums, key=lambda x: x == 0)
