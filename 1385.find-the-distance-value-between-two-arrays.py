class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        _bads = set([b for i in arr2 for b in range(i-d, i+d+1)])
        return sum([i not in _bads for i in arr1])
