class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        _r = set()
        for i in nums:
            _r.add(i)
            _r.add(float(str(i)[::-1]))
        return len(_r)
