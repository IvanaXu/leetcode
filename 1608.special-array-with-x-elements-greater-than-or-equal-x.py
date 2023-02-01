class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for n in range(len(nums)+1):
            if n == sum([i >= n for i in nums]):
                return n
        return -1
