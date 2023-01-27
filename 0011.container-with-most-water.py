class Solution:
    def maxArea(self, height: List[int]) -> int:
        # TODO: /
        l1 = len(height)
        l2 = l1 - 1
        result,n = 0, 0

        if height[0] > height[-1]:
            height = height[::-1]

        for i in range(l1):
            for j in range(l1-n):
                if l2-j-i > 0:
                    rmin = min(height[i], height[l2-j])
                    rcal = (l2-j-i) * rmin
                    if rcal > result:
                        result = rcal
                    
                    if rmin == height[i]:
                        break
                    if rmin == height[l2-j]:
                        n += 1
        return result
