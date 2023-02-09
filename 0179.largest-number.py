class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(sorted(
            map(str, nums),
            key=lambda x: x * (100 if len(x) == 1 else 2),
            reverse=True
        ))))
