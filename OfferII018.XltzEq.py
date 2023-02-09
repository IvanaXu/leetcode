class Solution:
    def isPalindrome(self, s: str) -> bool:
        _c = "abcdefghijklmnopqrstuvwxyz0123456789"
        _s = [i for i in s.lower() if i in _c]
        return _s == _s[::-1]
