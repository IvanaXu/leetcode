class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = [
            i for i in s.lower()
            if 48 <= ord(i) <= 57 or 97 <= ord(i) <= 122
        ]
        return _s == _s[::-1]
