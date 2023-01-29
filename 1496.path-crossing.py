class Solution:
    def isPathCrossing(self, path: str) -> bool:
        point, passl = (0, 0), [(0, 0)]
        for p in path:
            if p == "N":
                point = (point[0], point[1]+1)
            elif p == "S":
                point = (point[0], point[1]-1)
            elif p == "E":
                point = (point[0]+1, point[1])
            elif p == "W":
                point = (point[0]-1, point[1])
            
            if point not in passl:
                passl.append(point)
            else:
                return True
        return False
