class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        _nums = sorted(nums, reverse=True)
        _l = len(_nums)
        for an in range(_l):
            for bn in range(_l):
                if bn > an:
                    for cn in range(_l):
                        if cn > bn:
                            a, b, c = _nums[an], _nums[bn], _nums[cn]
                            if (a+b)>c and (a+c)>b and (b+c)>a:
                                return a+b+c
                            break
                    break
        return 0

