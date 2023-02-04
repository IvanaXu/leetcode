N = set("02468")
class Solution:
    def largestOddNumber(self, num: str) -> str:
        _r = len(num)
        for v in num[::-1]:
            if v in N:
                _r -= 1
            else:
                break
        return num[:_r]
