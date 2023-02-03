class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        return sum([
            (_f[1]//limit + (0 if _f[1]%limit == 0 else 1)) * time[_f[0]]
            for _f in fruits
        ])
