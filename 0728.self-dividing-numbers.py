class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [
            n for n in range(left, right+1)
            if "0" not in str(n) and sum([n%int(i) for i in str(n)]) == 0
        ]
