class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        p0, p1 = [], []
        for p in paths:
            p0.append(p[0])
            p1.append(p[1])
        return [p for p in p1 if p not in p0][0]
