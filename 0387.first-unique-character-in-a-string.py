class Solution:
    def firstUniqChar(self, s: str) -> int:
        _l = len(s)
        for n in range(_l):
            if s[n] not in s[n+1:] and s[n] not in s[:n]:
                return n
        return -1
