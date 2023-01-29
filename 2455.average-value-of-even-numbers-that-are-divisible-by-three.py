class Solution:
    def averageValue(self, nums: List[int]) -> int:
        _r = [n for n in nums if n%6 == 0]
        return int(sum(_r)/len(_r)) if _r else 0
