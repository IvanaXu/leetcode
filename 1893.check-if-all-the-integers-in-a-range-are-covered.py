class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return set([
            n for r in ranges
            for n in range(r[0], r[1]+1)
        ]).issuperset(set([
            n for n in range(left, right+1)
        ]))
