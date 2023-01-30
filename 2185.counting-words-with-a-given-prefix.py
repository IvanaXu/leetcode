class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = 0
        for w in words:
            if w.startswith(pref):
                n += 1
        return n
