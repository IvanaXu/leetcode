class MinStack:

    def __init__(self):
        self._l = []

    def push(self, val: int) -> None:
        self._l.append(val)

    def pop(self) -> None:
        self._l.pop()

    def top(self) -> int:
        return self._l[-1]

    def getMin(self) -> int:
        return min(self._l)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
