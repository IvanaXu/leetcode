class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        _k, _l = "left", len(arr)
        if _l < 3:
            return False
        for n in range(_l-1):
            v0, v1 = arr[n], arr[n+1]
            if _k == "left":
                if v0 == v1:
                    return False
                elif v0 > v1:
                    if n == 0:
                        return False
                    _k = "right"
            elif _k == "right":
                if v0 <= v1:
                    return False
        return _k != "left"
