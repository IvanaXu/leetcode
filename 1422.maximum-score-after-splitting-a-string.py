class Solution:
    def maxScore(self, s: str) -> int:
        return max([
            s[:n].count("0") + s[n:].count("1")
            for n in range(1, len(s))
        ])
