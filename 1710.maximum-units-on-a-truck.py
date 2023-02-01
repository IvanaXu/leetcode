class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        _s = 0
        for b in sorted(boxTypes, reverse=True, key=lambda x: (x[1], x[0])):
            bn, bw = b[0], b[1]
            
            cn = min([bn, truckSize])
            truckSize -= cn
            _s += (cn * bw)

            if truckSize == 0:
                break
        return _s
