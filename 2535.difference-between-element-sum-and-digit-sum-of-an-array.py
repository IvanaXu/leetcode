class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(
            sum(nums) - sum([int(i) for i in "".join([str(i) for i in nums])])
        )
