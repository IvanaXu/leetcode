class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        for n in range(len(s), 0, -1):
            if ("1" * n) in s and s.count("1") == n:
                return True
        return False
