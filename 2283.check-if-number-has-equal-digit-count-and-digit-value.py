class Solution:
    def digitCount(self, num: str) -> bool:
        for n, v in enumerate(num):
            if num.count(str(n)) != int(v):
                return False
        return True
