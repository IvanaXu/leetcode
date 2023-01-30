class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c, _hl = "aeiouAEIOU", len(s)//2
        return sum(
            [i in c for i in s[:_hl]]
        ) == sum(
            [i in c for i in s[_hl:]]
        )
