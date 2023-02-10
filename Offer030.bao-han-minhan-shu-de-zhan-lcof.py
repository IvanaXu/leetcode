class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._l = []

    def push(self, x: int) -> None:
        self._l.append(x)

    def pop(self) -> None:
        self._l.pop()

    def top(self) -> int:
        return self._l[-1]

    def min(self) -> int:
        return min(self._l)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
