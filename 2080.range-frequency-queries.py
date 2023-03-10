# 3688 ms
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self._r = {}

    def query(self, left: int, right: int, value: int) -> int:
        _k = f"{left}-{right}-{value}"# (left, right, value)
        if _k not in self._r:
            _v = self.arr[left: right+1].count(value)
            self._r[_k] = _v
            return _v
        else:
            return self._r[_k]




# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

# 616 ms
class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self._r = {}
        self._b = defaultdict(list)
        for n, v in enumerate(arr):
            self._b[v].append(n)

    def query(self, left: int, right: int, value: int) -> int:
        _k = (left, right, value)
        if _k not in self._r:
            _v = bisect_right(self._b[value],right) - bisect_left(self._b[value],left)
            self._r[_k] = _v
            return _v
        else:
            return self._r[_k]



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
