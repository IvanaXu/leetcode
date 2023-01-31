class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        _r = {}
        for i in nums:
            if i not in _r:
                _r[i] = 1
            else:
                _r[i] += 1
        return sum([_k for _k, _v in _r.items() if _v == 1])
