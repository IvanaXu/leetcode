class SortedStack:

    def __init__(self):
        import bisect
        self.q = []

    def push(self, val: int) -> None:
        bisect.insort(self.q, val)

    def pop(self) -> None:
        if not self.isEmpty():
            self.q.pop(0)

    def peek(self) -> int:
        return -1 if self.isEmpty() else self.q[0]

    def isEmpty(self) -> bool:
        return len(self.q) == 0

# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
