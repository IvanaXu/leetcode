class Solution:
    def massage(self, nums: List[int]) -> int:
        # 小偷系列: 198 213 337
        a, b = 0, 0
        for v in nums:
            print(a, b)
            c = b if b > a+v else a+v
            a = b
            b = c
        return b
