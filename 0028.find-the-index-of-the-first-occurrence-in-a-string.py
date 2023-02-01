class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for n, v in enumerate(haystack):
            if haystack[n:].startswith(needle):
                return n
        return -1
