class Solution:
    def findString(self, words: List[str], s: str) -> int:
        for n, v in enumerate(words):
            if v and v == s:
                return n
        return -1
