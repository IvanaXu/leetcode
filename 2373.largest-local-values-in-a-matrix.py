class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, N = len(grid)-2, 3
        return [
            [
                max([
                    max(i[n2: n2+N])
                    for n, i in enumerate(grid) 
                    if n1 <= n < n1+N
                ])
                for n2 in range(n)
            ]
            for n1 in range(n)
        ]
