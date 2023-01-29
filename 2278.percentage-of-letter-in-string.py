class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c, n = 0, 0
        for _s in s:
            if _s == letter:
                c += 1
            n += 1
        return int(c/n*100)
