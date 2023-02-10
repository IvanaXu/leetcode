class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        self.q.append(val)
        self.q.sort()
        self.q = self.q[-self.k:]
        return self.q[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
