class MaxQueue:

    def __init__(self):
        self.q = []

    def max_value(self) -> int:
        return max(self.q) if self.q else -1

    def push_back(self, value: int) -> None:
        self.q.append(value)

    def pop_front(self) -> int:
        return self.q.pop(0) if self.q else -1


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
