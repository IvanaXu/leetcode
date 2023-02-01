gets = lambda x: str(sum([int(i) for i in x]))
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while True:
            if len(s) <= k:
                return s
            
            s = "".join([
                gets(i) for i in [
                    s[n:n+k] for n in range(0, len(s), k)
                ]
            ])
