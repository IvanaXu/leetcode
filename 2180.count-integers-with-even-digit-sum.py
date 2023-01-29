class Solution:
    def countEven(self, num: int) -> int:
        return sum([
            sum([int(j) for j in str(i)])%2 == 0
            for i in range(1, num+1)
        ])
