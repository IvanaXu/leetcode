# https://leetcode.cn/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
