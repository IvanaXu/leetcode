class Solution:
    def trimMean(self, arr: List[int]) -> float:
        _l = len(arr)
        arr.sort()
        return sum(arr[_l//20:_l-_l//20])/(_l//20*18)
