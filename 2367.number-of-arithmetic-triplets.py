class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        _l = len(nums)
        return len([
            [i, j, k]
            for i in range(_l)
            for j in range(_l)
            for k in range(_l)
            if 
                i < j and 
                j < k and
                (nums[j] - nums[i]) == diff and
                (nums[k] - nums[j]) == diff
        ])
