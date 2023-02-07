class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 已经排序, 首尾双指针, 其和过大就可以继续寻找
        _l = len(numbers)
        i, j = 0, _l-1
        while i < j:
            vi, vj = numbers[i], numbers[j]
            if vi + vj > target:
                j -= 1 # i已经最小，但是过大，需要j小一点
            elif vi + vj < target:
                i += 1 # j已经最大，仍然不过，需要i大一点
            else:
                return [i+1, j+1]
