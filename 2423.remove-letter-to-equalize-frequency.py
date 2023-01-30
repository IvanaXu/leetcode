class Solution:
    def equalFrequency(self, word: str) -> bool:
        for n, v in enumerate(word):
            _word = f"{word[:n]}{word[n+1:]}"
            
            if len(set([_word.count(i) for i in set(_word)])) == 1:
                return True
        return False
