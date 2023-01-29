class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return not(word != word.upper() and word[1:] != word[1:].lower())
