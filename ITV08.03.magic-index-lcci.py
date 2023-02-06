class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for n, v in enumerate(nums):
            if n == v:
                return n
        return -1
