class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        _r, _num = [], ""
        for v in nums:
            _num += f"{v}"
            _r.append(int(str(_num), 2) % 5 == 0)
        return _r
