class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for n in range(len(sequence), 0, -1):
            if (n * word) in sequence:
                return n
        return 0
