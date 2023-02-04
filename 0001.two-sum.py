class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n, v in enumerate(nums):
            try:
                return [n, nums[n+1:].index(target-v)+n+1]
            except:
                pass
