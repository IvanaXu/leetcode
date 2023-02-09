class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        _r = "".join(
            sorted(map(str, nums),
            key=lambda x: x * (100 if len(x) == 1 else 2),
            reverse=True
        ))
        return f"{int(_r)}"
