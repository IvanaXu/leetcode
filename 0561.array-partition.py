class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # [6,2,6,5,1,2] > [1,2,2,5,6,6] > [1,2],[2,5],[6,6]
        # sort & split
        _l, _nums = len(nums), sorted(nums)
        return sum([
            min(_nums[n:n+2]) 
            for n in range(0, _l, 2)
        ])
