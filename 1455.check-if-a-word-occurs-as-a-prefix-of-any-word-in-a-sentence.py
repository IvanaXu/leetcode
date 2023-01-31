class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for n, v in enumerate(sentence.split(" ")):
            if v.startswith(searchWord):
                return n+1
        return -1
