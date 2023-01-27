class Solution:
    def countDigits(self, num: int) -> int:
        return len([
            int(i)
            for i in str(num)
            if num % int(i) == 0
        ])
