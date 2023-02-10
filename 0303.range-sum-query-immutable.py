class NumArray:

    def __init__(self, nums: List[int]):
        self.q = {0: 0}
        for n, v in enumerate(nums):
            self.q[n+1] = self.q[n] + v
    
    def sumRange(self, left: int, right: int) -> int:
        return self.q.get(right+1, 0) - self.q.get(left, 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
