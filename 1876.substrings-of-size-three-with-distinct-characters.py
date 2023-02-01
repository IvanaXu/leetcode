N = 3
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return len([
            s[n:n+N] for n in range(0, len(s)-N+1)
            if len(set(s[n:n+N])) == N
        ])
