class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Q = []

    def push(self, x: int) -> None:
        self.Q.append(x)

    def pop(self) -> None:
        self.Q.pop()

    def top(self) -> int:
        return self.Q[-1]

    def getMin(self) -> int:
        return min(self.Q)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
