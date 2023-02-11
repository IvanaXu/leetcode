class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1, l2 = [], []
        for v in nums:
            if v > 0:
                l1.append(v)
            else:
                l2.append(v)
        return [
            i for l in zip(l1, l2) 
            for i in l
        ]
