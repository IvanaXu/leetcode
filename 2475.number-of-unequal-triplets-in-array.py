class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        _l = len(nums)
        return len([
            [i, j, k]
            for i in range(_l)
            for j in range(_l)
            for k in range(_l)
            if 
                i < j and 
                j < k and 
                nums[i] != nums[j] and
                nums[i] != nums[k] and
                nums[j] != nums[k]
        ])
