class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for k in range(1, len(words)+1):
            if "".join(words[:k]) == s:
                return True
        return False
