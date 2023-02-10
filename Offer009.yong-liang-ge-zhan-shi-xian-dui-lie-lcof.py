class CQueue:

    def __init__(self):
        self.q = []

    def appendTail(self, value: int) -> None:
        self.q.append(value)

    def deleteHead(self) -> int:
        if not self.q:
            return -1
        else:
            _r = self.q[0]
            self.q.pop(0)
            return _r

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
