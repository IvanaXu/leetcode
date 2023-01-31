class Solution:
    def checkString(self, s: str) -> bool:
        for n, v in enumerate(s):
            if v == "b" and "a" in s[n:]:
                return False
        return True
