class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        _r = {i: set() for i in range(len(matrix))}
        
        for imatrix in matrix:
            _this = set()
            for ni, vi in enumerate(imatrix):
                # 
                if vi not in _this:
                    _this.add(vi)
                else:
                    return False
                # 
                if vi not in _r[ni]:
                    _r[ni].add(vi)
                else:
                    return False
            # if _m != sorted(_this):
            #     return False
        return True
