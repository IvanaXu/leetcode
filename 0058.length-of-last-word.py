class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = 0
        for i in s.rstrip(" ")[::-1]:
            if i == " ":
                break
            n += 1
        return n
