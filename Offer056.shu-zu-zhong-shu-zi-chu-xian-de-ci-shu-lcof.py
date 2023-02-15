class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        _r1, _rm = set(), set()
        for i in nums:
            if i not in _r1:
                _r1.add(i)
            else:
                _rm.add(i)
        return list(_r1-_rm)
