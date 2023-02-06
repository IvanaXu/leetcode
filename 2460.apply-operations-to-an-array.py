class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for n in range(len(nums)-1):
            if nums[n] == nums[n+1]:
                nums[n] = 2 * nums[n]
                nums[n+1] = 0
        return sorted(nums, key=lambda x: x == 0)
