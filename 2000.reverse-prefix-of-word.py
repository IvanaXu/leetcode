class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        _k = word.index(ch)+1
        return word[:_k][::-1] + word[_k:]
