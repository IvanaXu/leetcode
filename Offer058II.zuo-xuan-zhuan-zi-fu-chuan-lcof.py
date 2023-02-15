# Python2
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:] + s[:n]

# Python3
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return f"{s[n:]}{s[:n]}"
