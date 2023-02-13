class Solution:
    def firstUniqChar(self, s: str) -> str:
        for n, v in enumerate(s):
            if v not in s[:n] and v not in s[n+1:]:
                return v
        return " "
