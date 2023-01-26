# https://leetcode.cn/problems/power-of-two/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return bin(n).rstrip("0") == "0b1"
        return bin(n).rstrip("0") == "0b1" if n%2 == 0 or n == 1 else False
