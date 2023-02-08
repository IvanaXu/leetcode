class RecentCounter(object):

    def __init__(self):
        self._r = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self._r.append(t)
        self._r = [i for i in self._r if i >= (t-3000)]
        return len(self._r)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
