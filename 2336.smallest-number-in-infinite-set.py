class SmallestInfiniteSet:

    def __init__(self):
        N = 1000
        self.q = set([i for i in range(1, N+1)])

    def popSmallest(self) -> int:
        _min = min(self.q)
        self.q.remove(_min)
        return _min

    def addBack(self, num: int) -> None:
        self.q.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
