class Solution:
    def findGCD(self, nums: List[int]) -> int:
        _min, _max = min(nums), max(nums)
        for i in [i for i in range(1, _min+1)][::-1]:
            if _min%i == 0 and _max%i == 0:
                return i
