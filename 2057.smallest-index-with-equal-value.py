class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for n, v in enumerate(nums):
            if n%10 == v:
                return n
        return -1
