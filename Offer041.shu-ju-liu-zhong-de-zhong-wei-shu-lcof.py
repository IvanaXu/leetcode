import bisect
class MedianFinder:

    def __init__(self):
        self.n = 0
        self.l, self.r = 0, 0
        self.s = []
    
    def addNum(self, num: int) -> None:
        self.n += 1
        self.l = self.n//2-1 if self.n%2 == 0 else self.n//2
        self.r = self.n//2
        bisect.insort(self.s, num)
        
    def findMedian(self) -> float:
        return (self.s[self.l] + self.s[self.r])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
