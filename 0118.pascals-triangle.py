# https://leetcode.cn/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = {}
        for i in range(numRows):
            if i == 0:
                r[i] = [1]
            elif i == 1:
                r[i] = [1, 1]
            elif i > 1:
                r[i] = [1]
                k = 0
                for j in r[i-1]:
                    if k > 0:
                        r[i].append(j+k)
                    k = j
                r[i].append(1)
        return list(r.values())
