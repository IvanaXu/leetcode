class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        return sum([
            max(i) 
            for i in zip(*[
                sorted(g, reverse=True) 
                for g in grid
            ])
        ])
