class Solution:
    def greatestLetter(self, s: str) -> str:
        c = "zyxwvutsrqponmlkjihgfedcba"
        C = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

        for n in range(26):
            if c[n] in s and C[n] in s:
                return C[n]
        return ""
