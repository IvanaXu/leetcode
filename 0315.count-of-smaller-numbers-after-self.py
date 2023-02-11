class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        import bisect
        _r, _t = [], []
        for v in nums[::-1]:
            p = bisect.bisect_left(_t, v)
            _r.append(p)
            _t.insert(p, v)
        return _r[::-1]

"""
https://leetcode.cn/problems/count-of-smaller-numbers-after-self/comments/173901
"""
