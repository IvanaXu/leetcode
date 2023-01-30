class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while True:
            if n == 0:
                return False
            elif n == 1:
                return True
            elif n % 4 == 0:
                n = n/4
            else:
                return False
