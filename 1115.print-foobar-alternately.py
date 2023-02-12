import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock_foo = threading.Lock()
        self.lock_bar = threading.Lock()
        self.lock_bar.acquire() #
    
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock_foo.acquire()
            printFoo()
            self.lock_bar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock_bar.acquire()
            printBar()
            self.lock_foo.release()
