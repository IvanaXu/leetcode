# Python2
# ImportError: No module named queue

# Python3
import queue
class Foo:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.q3 = queue.Queue()
        self.q1.put("1")

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.q1.get()
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.q2.put("2")

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q2.get()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.q3.put("3")

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q3.get()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
