class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # (x - x0)^2 + (y - y0)^2 = r^2
        return [
            sum([
                (x-_x0)*(x-_x0) + (y-_y0)*(y-_y0) <= _r0*_r0
                for (x, y) in points
            ])
            for (_x0, _y0, _r0) in queries
        ]
