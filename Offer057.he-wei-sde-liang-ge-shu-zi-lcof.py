class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _l = len(nums)
        i, j = 0, _l-1
        while i < j:
            v = nums[i] + nums[j]
            if v > target:
                j -= 1
            elif v < target:
                i += 1
            else:
                return [nums[i], nums[j]]
