class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # https://leetcode.cn/problems/largest-number/
        return ''.join(sorted(
            map(str, nums),
            key=lambda x: x * (10 if len(x) == 1 else 2),
        ))
