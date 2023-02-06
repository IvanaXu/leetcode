# Python2
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.nums = []


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.nums) >= self.size:
            self.nums.pop(0)
        self.nums.append(val)
        return sum(self.nums)/float(len(self.nums))



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Python3
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.nums = []


    def next(self, val: int) -> float:
        if len(self.nums) >= self.size:
            self.nums.pop(0)
        self.nums.append(val)
        return mean(self.nums)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
