class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([_1!=_2 for _1, _2 in zip(heights, sorted(heights))])
