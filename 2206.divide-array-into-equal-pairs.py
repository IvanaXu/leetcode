class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = []
        for n in sorted(nums):
            if n not in c:
                if len(c)%2 == 1:
                    return False
                c = []
            c.append(n)
        return True
