class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        return sum([
            n1 < n2 and abs(v1-v2) == k
            for n1, v1 in enumerate(nums)
            for n2, v2 in enumerate(nums)
        ])
