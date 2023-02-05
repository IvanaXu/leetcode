class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def mySqrt(x: int) -> int:
            eps = 0.00000001
            low, last = 0, 0
            
            up = x
            mid = (low + up)/2
            while abs(mid - last) > eps:
                if mid * mid > x:
                    up = mid
                else:
                    low = mid
                last = mid
                mid = (up + low)/2
            return int(mid + eps)
        return num == mySqrt(num)**2
